*** Settings ***
Resource    src/resources/get_env.robot
Resource    src/resources/resource.robot

Test Setup      Open Connection To SMTP
Test Teardown   Close Connection


*** Variables ***
${FROM}       LOCAL_SENDER
${TO}         REMOTE_RECIPIENT
${SUBJECT}    Test subject
${BODY}       Test body



*** Test Cases ***
Test Successful Email Delivery TC05
    Load Environment Variables

    ${output}=    Send Mail
    ...           ${FROM}
    ...           ${TO}
    ...           ${SUBJECT}
    ...           ${BODY}


    Should Contain    ${output}    250
    Should Contain    ${output}    354
