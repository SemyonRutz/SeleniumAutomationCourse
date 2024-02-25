*** Settings ***
Library           SeleniumLibrary

*** Variables ***
${HOME PAGE URL}  http://demostore.supersqa.com/
${SEARCH FIELD ID}  woocommerce-product-search-field-0
${EXISTING ITEM SEARCH TERM}  album
${EXPECTED URL TEXT}  http://demostore.supersqa.com/product/album/
${ASCI CODE FOR ENTER}  \ue007

${NONE EXISTING ITEM SEARCH TERM}  nonexistingitem
${MSG BOX CLASS}  woocommerce-products-header__title
${NOT FOUND MSG}  Search results: “${NONE EXISTING ITEM SEARCH TERM}”

*** Test Cases ***
User should be able to search for existing product

    Open Browser  about:blank  chrome
    Go To  ${HOME PAGE URL}
    Input Text  ${SEARCH FIELD ID}  ${EXISTING ITEM SEARCH TERM}
    Press Keys  ${SEARCH FIELD ID}  ${ASCI CODE FOR ENTER}
    Location Should Contain  ${EXPECTED URL TEXT}
    Close Browser

User should see correct message when searching for non-existing product

    Open Browser  about:blank  chrome
    Go To  ${HOME PAGE URL}
    Input Text  ${SEARCH FIELD ID}  ${NONE EXISTING ITEM SEARCH TERM}
    Press Keys  ${SEARCH FIELD ID}  ${ASCI CODE FOR ENTER}
    Element Text Should Be  class=${MSG BOX CLASS}  ${NOT FOUND MSG}
    Close Browser


    
    