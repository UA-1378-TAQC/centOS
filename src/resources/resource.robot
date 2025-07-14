*** Settings ***
Library     SSHLibrary

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

Check Recipient Mailbox
    [Arguments]    ${recipient}
    ${username}=    Evaluate    "${recipient}".split("@")[0]
    ${result}=    Run Keyword And Return Status
    ...    SSHLibrary.Execute Command    test -s /var/spool/mail/${username}
    [Return]    ${result}

Verify Email Content
    [Arguments]    ${recipient}    ${expected_subject}    ${expected_body}
    ${username}=    Evaluate    "${recipient}".split("@")[0]
    
    ${mail_files}=    SSHLibrary.Execute Command    ls -t ${EMAIL_DIR}
    ${mail_filename}=    Evaluate    """${mail_files}.splitlines()[0]"""
    ${mail_content}=    SSHLibrary.Execute Command    cat ${EMAIL_DIR}/${mail_filename}
    
    ${subject_found}=    Run Keyword And Return Status
    ...    Should Contain    ${mail_content}    Subject: ${expected_subject}
    ${body_found}=    Run Keyword And Return Status
    ...    Should Contain    ${mail_content}    ${expected_body}
    ${content_valid}=    Evaluate    ${subject_found} and ${body_found}
    [Return]    ${content_valid}
