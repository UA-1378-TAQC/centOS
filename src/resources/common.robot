*** Settings ***
Library    OperatingSystem
Library    ../libraries/smtp_library.py

*** Keywords ***
Connect Smtp Server
    [Arguments]    ${HOST}    ${SMTP_PORT}=25
    ${SMTP_SRV}=    Connect Server    ${HOST}    ${SMTP_PORT}
    [Return]    ${SMTP_SRV}

Send Quit Command
    [Arguments]    ${SMTP_SRV}
    @{RESPONSE_MSG}=    Make Quit    ${SMTP_SRV}
    [Return]    @{RESPONSE_MSG}

Log In To Server
    [Arguments]    ${USER}    ${password}    ${SMTP_SRV}
    @{AUTH_RESPONSE}=    Login Server    ${USER}    ${password}    ${SMTP_SRV}
    [Return]    ${AUTH_RESPONSE}[0]

Check Hostname
    [Arguments]    ${HOSTNAME}    ${SMTP_SRV}
    @{response}=    Validate Hostname    ${HOSTNAME}    ${SMTP_SRV}
    Should Be Equal    ${response}[0]    ${250}

Send Message Via Host
    [Arguments]    ${HOST}    ${FROM_ADDR}    ${TO_ADDR}    ${MESSAGE}
    ${SMTP_SRV}=    Connect Server    ${HOST}
    Send Message Smtp    ${FROM_ADDR}    ${TO_ADDR}    ${MESSAGE}    ${SMTP_SRV}

Open Recent Mail
    [Arguments]    ${HOST}    ${USER}    ${PASS}
    ${RECEIVED_MAIL}    Read Recent Mail    ${USER}    ${PASS}    ${HOST}
    [Return]    ${RECEIVED_MAIL}

Form A Letter For Sending
    [Arguments]    ${message}    ${FROM_ADDR}    ${TO_ADDR}    ${SUBJ}='Test message1'
    ${LETTER_UTF8}=    Form Letter With Utf8    ${message}    ${FROM_ADDR}    ${TO_ADDR}    ${SUBJ}
    [Return]    ${LETTER_UTF8}

Check Recipient Domain
    [Arguments]    ${HOST}    ${SMTP_PORT}    ${FROM_ADDR}    ${TO_ADDR}
    @{RESPONSE}=    Verify Recipient Domain    ${HOST}    ${SMTP_PORT}    ${FROM_ADDR}    ${TO_ADDR}
    [Return]    @{RESPONSE}
    
Check Maillog
    [Arguments]    ${HOST}    ${USER}    ${PASS}
    ${OUTPUT}=    Read Log File    ${HOST}    ${USER}    ${PASS}
    [Return]    ${OUTPUT}
    