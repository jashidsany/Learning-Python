lovely_loveseat_description = """Lovely Loveseat: Tufted polyester blend on wood. 32 inches high x 40 inches wide x 30 inches deep. Red or white. """
lovely_loveseat_price = 254.00

stylish_settee_description = """Stylish Settee: Faux leather on birch. 29.50 inches high x 54.75 inches wide x 28 inches deep. Black. """
stylish_settee_price = 185.50

luxurious_lamp_description = """Luxurious Lamp: Glass and iron. 36 inches tall. Brown with cream shade. """
luxrious_lamp_price = 52.12

sales_tax = .088 # sales tax is 8.8%

customer_one_itemization = "1. " + lovely_loveseat_description  + "\n2. " + luxurious_lamp_description

customer_one_total = 0
customer_one_total += lovely_loveseat_price + luxrious_lamp_price + sales_tax

print("Customer One Items: ")
print(customer_one_itemization)
print("\nCustomer One Total: ")
print(customer_one_total)
