

def verify_discount_configs(original_price, discounted_price, applyied_discount):

    cleaned_original_price = float(original_price.replace("$", ""))
    cleaned_discounted_price = float(discounted_price.replace("$", ""))
    applyied_discount = float(applyied_discount)


    discount = cleaned_original_price*(applyied_discount/100)
    expected_discounted_price = cleaned_original_price - discount

    if expected_discounted_price != cleaned_discounted_price: 

        return f""" Discounted price is not as expected. 
    Original Price: {cleaned_original_price}, Applied Discount: {applyied_discount},
    Expected discounted price: {expected_discounted_price}, Actual discounted price: {cleaned_discounted_price} """

    else:
        return "Discounted price is as expected"