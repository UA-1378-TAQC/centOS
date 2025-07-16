*** Settings ***
Resource    ../resources/get_env.robot
Resource    ../resources/resource.robot

Test Setup      Open Connection To SMTP
Test Teardown   Close Connection

*** Variables ***
${SUBJECT}    Test subject
${BODY}       Test body

*** Test Cases ***
TC05: Verify Successful Email Delivery & Mailbox Content Validation
    Load Environment Variables

     ${output}=    Send Mail
    ...           ${SENDER}
    ...           ${RECIPIENT}
    ...           ${SUBJECT}
    ...           ${BODY}

    Should Contain    ${output}    220
    Should Contain    ${output}    250-mail.example.com
    Should Contain    ${output}    250-PIPELINING
    Should Contain    ${output}    250 2.1.0 Ok
    Should Contain    ${output}    354
    Should Contain    ${output}    250 2.0.0 Ok
    Should Contain    ${output}    221

    ${mail_check}=    Check Recipient Mailbox    ${RECIPIENT}
    Should Be True    ${mail_check}

    ${content_check}=    Verify Email Content    ${RECIPIENT}    ${SUBJECT}    ${BODY}
    Should Be True    ${content_check}
