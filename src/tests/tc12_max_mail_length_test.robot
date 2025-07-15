*** Settings ***
Resource    ../resources/get_env.robot
Resource    ../resources/resource.robot

Test Setup      Open Connection To SMTP
Test Teardown   Close Connection

*** Variables ***
${SUBJECT}                Test Max Line Length
${BODY_998_CHARS}         ${EMPTY}
${BODY_999_CHARS}         ${EMPTY}
${LINE_998_CHARS}         ${EMPTY}
${LINE_999_CHARS}         ${EMPTY}

*** Test Cases ***
TC12: Max Line Length in DATA (998 characters + CRLF)
    Load Environment Variables

    Log    Connection established and authenticated

    ${line_998}=    Generate Line Of Length    998
    ${line_999}=    Generate Line Of Length    999
    Set Test Variable    ${LINE_998_CHARS}    ${line_998}
    Set Test Variable    ${LINE_999_CHARS}    ${line_999}

    ${test_body}=    Catenate    SEPARATOR=\r\n
    ...    Line with exactly 998 characters:
    ...    ${LINE_998_CHARS}
    ...    Line with 999 characters (exceeds RFC 5321 recommendation):
    ...    ${LINE_999_CHARS}
    ...    End of test message

    Set Test Variable    ${BODY_998_CHARS}    ${test_body}

    ${output}=    Send Mail
    ...           ${SENDER}
    ...           ${RECIPIENT}
    ...           ${SUBJECT}
    ...           ${test_body}

    Should Contain    ${output}    220
    Should Contain    ${output}    250-mail.example.com
    Should Contain    ${output}    250-PIPELINING
    Should Contain    ${output}    250 2.1.0 Ok
    Should Contain    ${output}    354

    Run Keyword And Continue On Failure    Should Contain    ${output}    250 2.0.0 Ok

    ${has_error}=    Run Keyword And Return Status    Should Contain    ${output}    5
    Run Keyword If    ${has_error}    Log    Server rejected message with error code

    Should Contain    ${output}    221

    ${mail_delivered}=    Run Keyword And Return Status    Check Recipient Mailbox    ${RECIPIENT}
    Run Keyword If    ${mail_delivered}    Log    Email with long lines was successfully delivered
    Run Keyword Unless    ${mail_delivered}    Log    Email with long lines was rejected or not delivered

TC12_Boundary_Test: Test Exact RFC 5321 Boundary
    Load Environment Variables

    ${line_998}=    Generate Line Of Length    998
    ${body_998}=    Catenate    SEPARATOR=\r\n
    ...    Testing RFC 5321 boundary:
    ...    ${line_998}
    ...    End of boundary test

    ${output_998}=    Send Mail
    ...               ${SENDER}
    ...               ${RECIPIENT}
    ...               RFC 5321 Boundary Test
    ...               ${body_998}

    Should Contain    ${output_998}    250 2.0.0 Ok
    Should Contain    ${output_998}    221

    ${line_999}=    Generate Line Of Length    999
    ${body_999}=    Catenate    SEPARATOR=\r\n
    ...    Testing beyond RFC 5321 boundary:
    ...    ${line_999}
    ...    End of boundary test

    ${output_999}=    Send Mail
    ...               ${SENDER}
    ...               ${RECIPIENT}
    ...               RFC 5321 Boundary Exceed Test
    ...               ${body_999}

    ${accepted_999}=    Run Keyword And Return Status    Should Contain    ${output_999}    250 2.0.0 Ok
    Run Keyword If    ${accepted_999}    Log    Server accepts lines longer than 998 characters
    Run Keyword Unless    ${accepted_999}    Log    Server rejects lines longer than 998 characters

*** Keywords ***
Generate Line Of Length
    [Arguments]    ${length}
    [Documentation]    Generate a line of text with exactly the specified length

    ${base_char}=    Set Variable    A
    ${repeated_chars}=    Evaluate    "${base_char}" * ${length}

    ${actual_length}=    Get Length    ${repeated_chars}
    Should Be Equal As Integers    ${actual_length}    ${length}

    [Return]    ${repeated_chars}


