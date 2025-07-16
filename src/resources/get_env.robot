*** Settings ***
Library    OperatingSystem
Library    ../libraries/load_env.py

*** Keywords ***
Load Environment Variables
    Load Envs
    ${HOST}=    Get Environment Variable    HOSTNAME
    ${PORT}=    Get Environment Variable    SMTP_PORT
    ${PORT_INT}=    Evaluate    int(${PORT})
    ${USER}=    Get Environment Variable    SSH_USERNAME
    ${PASS}=    Get Environment Variable    SSH_PASSWORD
    ${TCP_TIMEOUT}=    Get Environment Variable    TCP_TIMEOUT
    ${SENDER}=    Get Environment Variable    LOCAL_SENDER
    ${RECIPIENT}=    Get Environment Variable    REMOTE_RECIPIENT
    ${EMAIL_DIR}=    Get Environment Variable    EMAIL_DIR
    ${SPAM_SENDER}=    Get Environment Variable    SPAM_SENDER

    Log    Loaded host: ${HOST}
    Log    Port: ${PORT_INT}

    Set Suite Variable    ${HOST}
    Set Suite Variable    ${PORT_INT}
    Set Suite Variable    ${TCP_TIMEOUT}
    Set Suite Variable    ${USER}
    Set Suite Variable    ${PASS}
    Set Suite Variable    ${SENDER}
    Set Suite Variable    ${RECIPIENT}
    Set Suite Variable    ${EMAIL_DIR}
    Set Suite Variable    ${SPAM_SENDER}
