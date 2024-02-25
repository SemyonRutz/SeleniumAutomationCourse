*** Settings ***
Library          SeleniumLibrary
Library          ssqatest.src.demostore.homepage.homepage

*** Test Cases ***
Home Page Should Have 16 Items Displayed

    Open Browser  about:blank  chrome
    Go to  http://demostore.supersqa.com/
    Verify 16 products are displayed
    Close Browser