*** Settings ***
Library    ../libraries/tcp_library.py
Resource   ../resources/get_env.robot

*** Keywords ***
Connect To Invalid Port Keyword
    [Arguments]    ${HOST}    ${WRONG_PORT_INT}    ${TCP_TIMEOUT}
    ${result}=    Connect To Invalid Port    ${HOST}    ${WRONG_PORT_INT}    ${TCP_TIMEOUT}
    [Return]    ${result}


Check HELO Command Response
    [Arguments]    ${HOST}    ${PORT_INT}
    ${result}=    Check Helo Response    ${HOST}    ${PORT_INT}
    [Return]    ${result}
