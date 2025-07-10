*** Settings ***
Resource    ../resources/get_env.robot
Resource    ../resources/common.robot

*** Variables ***

*** Test Cases ***
Quit From Server
    Load Environment Variables
    ${SMTP_SVR}=   Connect Smtp Server    ${HOST}    ${PORT_INT}
    @{RESULT}=    Send Quit Command    ${SMTP_SVR}
    Should Be Equal    ${RESULT}[1]    2.0.0 Bye
    