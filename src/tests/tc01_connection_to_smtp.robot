*** Settings ***
Library    ../libraries/tcp_library.py
Resource   ../resources/get_env.robot
Resource   ../resources/tcp_keywords.robot


*** Test Cases ***
Verify SMTP Server Connection
    Load Environment Variables
    ${result}=    Verify SMTP Greeting Response    ${HOST}    ${PORT_INT}
    Should Be Equal    ${result}    GREETING_OK
