*** Settings ***
Resource    ../resources/get_env.robot
Resource    ../resources/resource.robot
Resource    ../resources/tb_keywords.robot

Test Setup      Open Connection To SMTP
Test Teardown   Close Connection

*** Variables ***
${SUBJECT998}             998 Boundary Test
${SUBJECT999}             999 Boundary Test

*** Test Cases ***
TC12: Verify Successful Email Delivery With 998 Characters Length in Body
    Load Environment Variables

    ${body_998}=    Generate Line Of Length    998

    ${output_998}=    Send Mail
    ...               ${SENDER}
    ...               ${RECIPIENT}
    ...               ${SUBJECT998}
    ...               ${body_998}

    Should Contain    ${output_998}    220
    Should Contain    ${output_998}    250-mail.example.com
    Should Contain    ${output_998}    250-PIPELINING
    Should Contain    ${output_998}    250 2.1.0 Ok
    Should Contain    ${output_998}    354

    ${mail_check}=    Check Recipient Mailbox    ${RECIPIENT}
    Should Be True    ${mail_check}

    ${content_check}=    Verify Email Content    ${RECIPIENT}    ${SUBJECT998}    ${body_998}
    Should Be True    ${content_check}

TC12 Verify Rejection Mail With 999 Char In Body  
    ${body_999}=    Generate Line Of Length    999

    ${output}=    Send Mail
    ...           ${SENDER}
    ...           ${RECIPIENT}
    ...           ${SUBJECT999}
    ...           ${body_999}

    Should Contain    ${output}    550
    Should Contain    ${output}    5.7.1
    Should Contain    ${output}    Message body too long
