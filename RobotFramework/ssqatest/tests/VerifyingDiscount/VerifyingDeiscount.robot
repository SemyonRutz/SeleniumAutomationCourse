*** Settings ***    
Library  SeleniumLibrary  implicit_wait=10
Library  SeleniumLibrary
Library  ssqatest.src.demostore.DemoStoreConfig.couponConfigs.ValidCoupons
Library  ssqatest.src.demostore.DemoStoreConfig.verifyingDiscountConfigs


*** Variables ***
${discount}  100


*** Test Cases ***
Valid disctoun should be applied

    Go to the home page
    Click on product and then cart
    Get a cuopon and input it
    Verifying applited coupon text is correct
    Close Browser




*** Keywords ***
Go to the home page
    Open Browser      about:blank  chrome
    Go To             http://demostore.supersqa.com/

Click on product and then cart
    Click Element     css:.post-24 .button
    Wait Until Element Contains  css:.count  1 item
    Click Element     css:li.page_item.page-item-7 > a

Get a cuopon and input it

    ${ValidCoupon}    Get a Valid Coupon
    Log               The valid coupon is: ${ValidCoupon}  console=True

    Input Text        id:coupon_code    ${ValidCoupon}
    Press Keys        id:coupon_code     \ue007

Verifying applited coupon text is correct
    ${succsess message}  Get Text  css:.woocommerce-message
    Log    ${succsess message}  console=True
    Should Be Equal    ${succsess message}    Coupon code applied successfully.

Verifying discount is correct
    sleep  1
    ${original_price}  Get Text  css:#post-7 tr.cart-subtotal .amount
    Log    ${original_price}  console=True
    ${discounted_price}  Get Text  css:#post-7 tr.order-total > td > strong
    Log    ${discounted_price}  console=True

    verify_discount_configs  ${original_price}    ${discounted_price}    ${discount}