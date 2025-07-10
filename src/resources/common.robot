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
