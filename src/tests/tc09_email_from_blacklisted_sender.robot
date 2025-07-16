*** Settings ***
Resource    ../resources/common.robot
Resource    ../resources/tb_keywords.robot
Resource    ../resources/resource.robot

Test Setup      Open Connection To SMTP
Test Teardown   Close Connection

*** Variables ***
${SUBJECT}    tc09
${BODY}    Sssspppppaaaaaammmm

*** Test Cases *** 
TC09 Email From Blacklisted Sender
    
    Load Environment Variables

    ${commands}=    Catenate    SEPARATOR=\n
    ...    MAIL FROM:${SPAM_SENDER}
    ...    RCPT TO:${RECIPIENT}
    ...    DATA
    ...    Subject:${SUBJECT}
    ...    
    ...    ${BODY}
    ...    .
    ...    QUIT

    ${smtp_response}=    SSHLibrary.Execute Command    echo -e "${commands}" \| nc ${HOST} ${PORT_INT}
    Log    ${smtp_response}

    Should Contain    ${smtp_response}    554 5.7.1
