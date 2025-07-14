import socket
import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from config.logger_config import setup_logger

def connect_to_invalid_port(host, port, timeout=5):
    """ Try to connect to a TCP port that is expected to be invalid."""
    logger = setup_logger(test_name="WrongPortTest")
    set_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    set_socket.settimeout(int(timeout))
    try:
        logger.info("Trying TCP connection to %s:%s with timeout %s" % (host, port, timeout))
        set_socket.connect((host, int(port)))
        set_socket.close()
        logger.info("TCP connection successful")
        return "CONNECTED"
    except Exception as e:
        logger.warn("TCP connection failed: %s" % str(e))
        return "CONNECTION_FAILED"

def check_helo_response(server_ip, server_port):
    """Send HELO command and verify server responds with code 250."""
    logger = setup_logger(test_name="HeloResponseTest")
    try:
        logger.info("Connecting to %s:%s" % (server_ip, server_port))
        set_socket = socket.create_connection((server_ip, int(server_port)), timeout=5)

        response = set_socket.recv(1024).decode('utf-8')
        logger.info("Server greeting: %s" % response.strip())

        helo_command = "HELO example.com\r\n"
        logger.info("Sending: %s" % helo_command.strip())
        set_socket.sendall(helo_command.encode('utf-8'))

        helo_response = set_socket.recv(1024).decode('utf-8').strip()
        logger.info("HELO response: %s" % helo_response)

        set_socket.close()

        if helo_response.startswith("250"):
            return "HELO_OK"
        else:
            return "HELO_FAILED: %s" % helo_response

    except Exception as e:
        logger.error("Error during HELO check: %s" % str(e))
        return "ERROR: %s" % str(e)
