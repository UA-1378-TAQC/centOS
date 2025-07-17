*** Settings ***
Resource    ../resources/get_env.robot
Resource    ../resources/common.robot
Resource    ../resources/tb_keywords.robot
Resource    ../resources/tcp_keywords.robot
Resource    ../resources/resource.robot

Test Setup    Open Connection To SMTP
Test Teardown    Close Connection

*** Variables ***
${SUBJECT}    TC10
${BODY}    Ip Address Blacklisting

*** Test Cases ***
TC10 Ip Address Blacklisting

    Load Environment Variables
        
    ${output}=    Send Mail
    ...    ${SENDER}
    ...    ${RECIPIENT}
    ...    ${SUBJECT}
    ...    ${BODY}

    Log To Console    ${output}

    # Should Contain    ${output}    250
    # Should Contain    ${output}    354

    # Should Contain    ${output}    554
    # Should Contain    ${output}    5.7.1
    # Should Contain    ${output}    Access denied
    
    ${res}=    Get Sender Ip    ${HOST}    ${PORT_INT}
    Log To Console    ${res}
