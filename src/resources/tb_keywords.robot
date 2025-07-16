*** Settings ***
Library    SSHLibrary
Library    Process
Library    OperatingSystem

Resource    ../resources/get_env.robot

*** Keywords ***
Connect To SMTP And Authenticate
    Load Environment Variables
    Open Connection    ${HOST}
    Login              ${USER}    ${PASS}

Test TCP connectivity
    ${connection_result}=    Execute Command    nc -vz ${HOST} ${SMTP_PORT} 2>&1
    [Return]    ${connection_result}

Send Line Of 998 Characters
    ${line_998}=    Evaluate    "A" * 998
    ${cmd}=    Set Variable    echo -e "EHLO ${HOST}\r\n MAIL FROM:<${SENDER}>\r\nRCPT TO:<${USER}>\r\nDATA\r\n${line_998}\r\n.\r\nQUIT\r\n" | nc ${HOST} ${PORT_INT}
    ${mail_result}=    Execute Command    ${cmd}
    [Return]    ${mail_result}

Send Line Of 999 Characters
    ${line_999}=    Evaluate    "A" * 999
    ${cmd}=    Set Variable    echo -e "EHLO ${HOST}\r\n MAIL FROM:<${SENDER}>\r\nRCPT TO:<${USER}>\r\nDATA\r\n${line_999}\r\n.\r\nQUIT\r\n" | nc ${HOST} ${PORT_INT}
    ${mail_result}=    Execute Command    ${cmd}
    [Return]    ${mail_result}

Send EHLO
    [Arguments]
    ${cmd}=    Set Variable    echo -e "EHLO ${HOST}\r\n" | nc ${HOST} ${PORT_INT}
    ${ehlo_result}=    Execute Command    ${cmd}
    [Return]    ${ehlo_result}

Send EHLO Wigh Arguments
    [Arguments]    ${port}
    ${cmd}=    Set Variable    echo -e "EHLO ${HOST}\r\n" | nc ${HOST} ${port}
    ${ehlo_result}=    Execute Command    ${cmd}
    [Return]    ${ehlo_result}

Provide Incorrect AUTH LOGIN
    ${inv_data_cmd}=    Set Variable    echo -e "AUTH LOGIN ${AUTH_STRING}\r\n" | nc ${HOST} ${PORT_INT}
    ${auth_result}=    Execute Command    ${inv_data_cmd}
    [Return]    ${auth_result}

Generate Line Of Length
    [Arguments]    ${length}

    ${base_char}=    Set Variable    A
    ${repeated_chars}=    Evaluate    "${base_char}" * ${length}

    ${actual_length}=    Get Length    ${repeated_chars}
    Should Be Equal As Integers    ${actual_length}    ${length}

    [Return]    ${repeated_chars}


