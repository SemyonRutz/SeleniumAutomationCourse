*** Settings ***
Documentation     This is a test suite for the My Account page
...               It will test the login functionality
...               ${/n} is used to create a new line


Library           SeleniumLibrary
Resource          C:/Users/srutz/OneDrive - Centuri Group, Inc/Documents/GitHub/RobotFramework/ssqatest/DemoStoreSuperSQA/src/demostore/myAccount/MyAccountVariables.robot
  
Test Setup  Run Keywords  Open Browser  about:blank  Chrome  AND  Go To  ${MY_ACCOUNT}
Test Teardown    Close Browser

*** Test Cases ***
User get the right message when trying to log in without password and username

    [Documentation]    User get the right message when trying to log in without password and username
    Click Button    ${LOGIN_BTN}
    ${founded_error}  Get Text    ${ERROR_MSG}    
    Should Be Equal As Strings  ${founded_error}  ${EXP_ERROR_MSG}


User get the right message when trying to log in without password and username

    Click Button    ${LOGIN_BTN}
    ${founded_error}  Get Text    ${ERROR_MSG}    
    Should Be Equal As Strings  ${founded_error}  ${EXP_ERROR_MSG}
User get the right message when trying to log in without password and username

    Click Button    ${LOGIN_BTN}
    ${founded_error}  Get Text    ${ERROR_MSG}    
    Should Be Equal As Strings  ${founded_error}  ${EXP_ERROR_MSG}
User get the right message when trying to log in without password and username


    Click Button    ${LOGIN_BTN}
    ${founded_error}  Get Text    ${ERROR_MSG}    
    Should Be Equal As Strings  ${founded_error}  ${EXP_ERROR_MSG}
User get the right message when trying to log in without password and username

    Click Button    ${LOGIN_BTN}
    ${founded_error}  Get Text    ${ERROR_MSG}    
    Should Be Equal As Strings  ${founded_error}  ${EXP_ERROR_MSG}
User get the right message when trying to log in without password and username

    Click Button    ${LOGIN_BTN}
    ${founded_error}  Get Text    ${ERROR_MSG}    
    Should Be Equal As Strings  ${founded_error}  ${EXP_ERROR_MSG}

