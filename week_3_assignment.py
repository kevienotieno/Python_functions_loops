def calculate_discount(price, discount_percent):
    if discount_percent >20:
        final_price = ((100-discount_percent)/100)*price
        print(f"The final price is {final_price}")
    else:
        final_price = price
        print(f"The final price is {final_price}")

price = float(input("Enter the price of the product: "))
discount_percent = float(input("Enter the discount on the product: "))

calculate_discount(price, discount_percent)

