from robot.api.deco import keyword

class ValidCoupons():

    @keyword(name="Get a Valid Coupon")
    def Get_Valid_Coupon(self):
        
        COUPON1 = "SSQA100"
        
        return COUPON1
