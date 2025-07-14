*** Settings ***
Library    ../libraries/smtp_library.py

Resource   ../resources/get_env.robot

*** Keywords ***

Send Email With Headers Only
    [Arguments]    ${SENDER}    ${RECIPIENT}    ${SUBJECT}    ${HOST}    ${PORT_INT}
    ${result}=    Send Email Headers Only    ${SENDER}    ${RECIPIENT}    ${SUBJECT}    ${HOST}    ${PORT_INT}
    [Return]    ${result}

Send Data Without Rcpt To
    [Arguments]    ${SENDER}    ${HOST}    ${PORT_INT}
    ${result}=    Send Data Without Rcpt    ${SENDER}   ${HOST}    ${PORT_INT}
    [Return]    ${result}
