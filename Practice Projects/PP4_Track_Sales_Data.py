# This program takes 3 variables and outputs a boolean value based on what is true and what is false.
stock = 600
jeans_sold = 500
target_hit = 500

target_hit = jeans_sold == target_hit
print("Hit jeans sale target: ")
print(target_hit)

current_stock = stock - jeans_sold
in_stock = current_stock != 0
print("Jeans in stock: ")
print(in_stock)
