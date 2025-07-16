*** Settings ***
Resource    ../resources/get_env.robot
Resource    ../resources/resource.robot
Resource    ../resources/tb_keywords.robot

Test Setup      Open Connection To SMTP
Test Teardown   Close Connection

*** Variables ***
${SUBJECT333}             333 Boundary Test
${SUBJECT334}             334 Boundary Test

*** Test Cases ***
TC12: Verify Successful Email Delivery With 333 Characters Length in Body
    Load Environment Variables

    ${body_333}=    Generate Line Of Length    333

    ${output_333}=    Send Mail
    ...               ${SENDER}
    ...               ${RECIPIENT}
    ...               ${SUBJECT333}
    ...               ${body_333}

    Should Contain    ${output_333}    220
    Should Contain    ${output_333}    250-mail.example.com
    Should Contain    ${output_333}    250-PIPELINING
    Should Contain    ${output_333}    250 2.1.0 Ok
    Should Contain    ${output_333}    354

    ${mail_check}=    Check Recipient Mailbox    ${RECIPIENT}
    Should Be True    ${mail_check}

    ${content_check}=    Verify Email Content    ${RECIPIENT}    ${SUBJECT333}    ${body_333}
    Should Be True    ${content_check}

TC12 Verify Rejection Mail With 334 Char In Body  
    ${body_334}=    Generate Line Of Length    334

    ${output}=    Send Mail
    ...           ${SENDER}
    ...           ${RECIPIENT}
    ...           ${SUBJECT334}
    ...           ${body_334}

    Should Contain    ${output}    550
    Should Contain    ${output}    5.7.1
    Should Contain    ${output}    Message body too long
