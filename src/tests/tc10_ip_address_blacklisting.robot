*** Settings ***
Resource    ../resources/common.robot
Resource    ../resources/get_env.robot
Resource    ../resources/resource.robot
Resource    ../resources/tcp_keywords.robot

Test Setup    Open Connection To SMTP
Test Teardown    Close Connection

*** Variables ***
${SUBJECT}    TC10
${BODY}    Ip Address Blacklisting
${SENDER_IP}    192.168.229.1
${SENDER_IP_BLACKLIST}    192.168.171.1

*** Test Cases ***
TC10 Ip Address Blacklisting

    Load Environment Variables

    ${result}=    Run Keyword And Ignore Error    Send Mail With Ip
    ...           ${SENDER}
    ...           ${RECIPIENT}
    ...           ${SUBJECT}
    ...           ${BODY}
    ...           ${SENDER_IP_BLACKLIST}
    ...           ${HOST}
    ...           ${PORT_INT}

    ${status}=    Set Variable    ${result[0]}
    ${output}=    Set Variable    ${result[1]}
    Log To Console    Status: ${status}
    Log To Console    Output:\n${output}

    Should Contain    ${output}    554
    Should Contain    ${output}    5.7.1
    Should Contain    ${output}    Blacklist Ip
