*** Settings ***
Resource    src/resources/get_env.robot
Resource    src/resources/resource.robot

Test Setup      Open Connection To SMTP
Test Teardown   Close Connection


*** Variables ***
${SUBJECT}    Test subject
${BODY}       Test body

*** Test Cases ***
Test Successful Email Delivery TC05
    Load Environment Variables

    ${output}=    Send Mail
    ...           ${SENDER}
    ...           ${RECIPIENT}
    ...           ${SUBJECT}
    ...           ${BODY}

    Should Contain    ${output}    250
    Should Contain    ${output}    354
