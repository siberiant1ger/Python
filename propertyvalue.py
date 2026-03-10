
TAX_FACTOR = 0.0065
lot = int(input("Enter your lot number:"))
while (lot != 0):
    price = int(input("What's the price of the item? "))
    total_price = price + (price * TAX_FACTOR)
    print(f"The total price is: {total_price:.2f}")
    print(f"The tax amount is: {(total_price - price):.2f}")
    lot = int(input("Enter your lot number"))

print("Thank you lil bro")