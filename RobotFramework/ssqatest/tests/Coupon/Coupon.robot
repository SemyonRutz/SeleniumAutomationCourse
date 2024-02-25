*** Settings ***    
Library  SeleniumLibrary  implicit_wait=10
Library  SeleniumLibrary
Library  ssqatest.src.demostore.DemoStoreConfig.couponConfigs.ValidCoupons


*** Test Cases ***
Valid coupon should show succsess message
    
    Open Browser      about:blank  chrome
    Go To             http://demostore.supersqa.com/
    Click Element     css:.post-24 .button
    Wait Until Element Contains  css:.count  1 item
    Click Element     css:li.page_item.page-item-7 > a

    ${ValidCoupon}    Get a Valid Coupon
    Log               The valid coupon is: ${ValidCoupon}  console=True


    Input Text        id:coupon_code    ${ValidCoupon}
    Press Keys        id:coupon_code     \ue007

    ${succsess message}  Get Text  css:.woocommerce-message
    Log    ${succsess message}  console=True
    Should Be Equal    ${succsess message}    Coupon code applied successfully.
    
    Close Browser