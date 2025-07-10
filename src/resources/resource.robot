*** Settings ***
Library    SSHLibrary
Library    Process
Library    OperatingSystem
Resource    ../resources/get_env.robot

*** Keywords ***
Open Connection To SMTP
     Load Environment Variables
     Log    Connecting to: ${HOST}:${PORT_INT}
     Open Connection    ${HOST}    22
     Login    ${USER}    ${PASS}

Close Connection With SMTP
    Close Connection

Send Mail
    [Arguments]    ${from}    ${to}    ${subject}    ${body}    ${ehlo}=example.com
    ${mail_commands}=    Catenate    SEPARATOR=\n
    ...    EHLO example.com
    ...    MAIL FROM:<${from}>
    ...    RCPT TO:<${to}>
    ...    DATA
    ...    Subject: ${subject}
    ...    From: ${from}
    ...    To: ${to}
    ...
    ...    ${body}
    ...    .
    ...    QUIT

    ${output}=    SSHLibrary.Execute Command    echo -e "${mail_commands}" \| nc ${HOST} ${PORT_INT}
    Log    ${output}
    [Return]    ${output}
