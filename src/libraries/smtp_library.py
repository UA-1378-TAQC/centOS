import os
import paramiko
import smtplib
import socket
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from config.logger_config import setup_logger

def connect_server(host, port=25):
    logger = setup_logger('ConnectionAttempt')
    try:
        logger.info("Connection attempt to host: %s" % host)
        smtp_server = smtplib.SMTP(host)
        logger.info("Connection to %s is set" % host)
        return smtp_server
    except smtplib.SMTPServerDisconnected:
        logger.warn("Cannot connect to host %s. Verify the host is available." % host)

def make_quit(smtp_svr):
    return smtp_svr.quit()

def send_email_headers_only(sender, recipient, subject, server_ip, server_port):
    """ Send an email with only headers (without body) to test SMTP server response."""
    logger = setup_logger(test_name="SendEmailHeadersOnlyTest")
    try:
        logger.info("Connecting to SMTP server at %s:%s", server_ip, server_port)
        server = smtplib.SMTP(server_ip, server_port)
        logger.info("Sending EHLO command")
        server.ehlo()
        server.mail(sender)
        server.rcpt(recipient)
        message = "From: %s\r\nTo: %s\r\nSubject: %s\r\n\r\n.\r\n" % (sender, recipient, subject)
        server.data(message)
        logger.info("Quitting SMTP session")
        server.quit()
        logger.info("Email sent successfully from %s to %s (headers only)", sender, recipient)
        return "EMAIL_SENT"
    except Exception as e:
        logger.error("Failed to send email: %s", str(e))
        return "SEND_FAILED: %s" % str(e)

def send_data_without_rcpt(sender, server_ip, server_port):
    """ Try to send DATA command without specifying RCPT TO.
    Expect the server to reject the request."""
    logger = setup_logger(test_name="SendDataWithoutRcptTest")
    try:
        logger.info("Connecting to SMTP server %s:%s" % (server_ip, server_port))
        server = smtplib.SMTP(server_ip, server_port)
        server.ehlo()

        logger.info("Sending MAIL FROM without RCPT TO")
        code, response = server.mail(sender)

        logger.info("Sending DATA without RCPT TO")
        code, response = server.docmd("DATA")
        if code != 354:
            logger.info("Correct behavior: Server rejected DATA. Response: %s %s" % (code, response))
            server.quit()
            return "REJECTED"
        else:
            logger.warn("Unexpected success: Server allowed DATA without RCPT TO. Response: %s %s" % (code, response))
            server.quit()
            return "UNEXPECTED_SUCCESS"

    except Exception as e:
        logger.error("General error: %s" % str(e))
        return "SEND_FAILED"

def verify_recipient_domain(host, port, sender, recipient):
    logger = setup_logger('SendDataToNonExistingRcpt')
    try:
        smtp_svr = smtplib.SMTP(host, port)
        smtp_svr.mail(sender)
        code, response = smtp_svr.rcpt(recipient)
        logger.info("Reply code rcpt TO: %d, %s" % ( code, response))
        if code == 250:
            try:
                smtp_svr.data('Test msg')
            except smtplib.SMTPDataError as e:
                logger.warn("Not valid recipient: %s" % recipient)
                smtp_svr.quit()
                return e.smtp_code, e.message
        else:
            smtp_svr.quit()
            return code, response
    except smtplib.SMTPRecipientsRefused as e:
        logger.warn("An invalid address for recipient: %s" % recipient)
        return e.message
    except smtplib.SMTPConnectError as e:
        logger.warn("Connection to %s is failed. Make sure that assigned port and hostname are correct" % host)
        return e.smtp_code, e.message


def validate_hostname(hostname, smtp_srv=smtplib.SMTP()):
    return smtp_srv.docmd('ehlo', hostname)

def form_letter_with_utf8(text, from_addr, to_addr, subject='Test message1'):
    msg = MIMEText(text, 'plain', 'utf-8')
    msg['From'] = from_addr
    msg['To'] = to_addr
    msg['Subject'] = subject

    return msg.get_payload(decode=True)

def login_server(username, passw, smtp_srv=smtplib.SMTP()):
    return smtp_srv.login(username, passw)

def send_message_smtp(from_addr, to_addr, message, smtp_srv=smtplib.SMTP()):
    logger = setup_logger("SendSmtpMessage")
    try:
        smtp_srv.verify(to_addr)
        reply = smtp_srv.sendmail(from_addr, to_addr, message)
        logger.info("The message is sent from %s to %s" % (from_addr, to_addr))
        return reply
    except smtplib.SMTPRecipientsRefused:
        logger.warn("Recipient address is invalid: %s" % to_addr)
    finally:
        logger.info("Quit command is executing...")
        smtp_srv.quit()

def read_recent_mail(username, password, host):
    session = paramiko.SSHClient()
    session.load_system_host_keys()
    session.connect(host, 22, username, password)
    _, stdout, _ = session.exec_command(
        "recent_mail=$(ls --sort=time /home/{}/Maildir/new/ | head -n 1) && cat /home/{}/Maildir/new/$recent_mail".format(
            username, username))
    return stdout.read()

def send_mail_with_ip_function(sender, recipient, subject, body, source_ip, host, port):
    class SMTPWithSourceIP(smtplib.SMTP):
        def _get_socket(self, host, port, timeout):
            return socket.create_connection((host, port), timeout, source_address=(source_ip, 0))

    try:
        smtp = SMTPWithSourceIP(timeout=10)
        smtp.connect(host, port)
        smtp.ehlo()

        message = "Subject: {}\r\nFrom: {}\r\nTo: {}\r\n\r\n{}".format(subject, sender, recipient, body)

        res = smtp.sendmail(sender, recipient, message)
        smtp.quit()

        return "SUCCESS: {}".format(res)

    except Exception as e:
        return "ERROR: {}".format(str(e))
