import smtplib

from robot.api.deco import keyword
from config.logger_config import setup_logger

@keyword
def connect_server(host, port=25):
    logger = setup_logger('ConnectionAttempt')
    try:
        logger.info("Connection attempt to host: %s" % host)
        smtp_server = smtplib.SMTP(host)
        logger.info("Connection to %s is set" % host)
        return smtp_server
    except smtplib.SMTPServerDisconnected:
        logger.warn("Cannot connect to host %s. Verify the host is available." % host)

@keyword
def make_quit(smtp_svr=smtplib.SMTP()):
    return smtp_svr.quit()
