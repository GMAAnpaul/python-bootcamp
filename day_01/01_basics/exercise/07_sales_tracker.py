# Ask the cost and pax or count for three separate items
item_cost_1 = None  # Let the user enter a number
item_count_1 = None  # Let the user enter a number

item_cost_2 = None  # Let the user enter a number
item_count_2 = None  # Let the user enter a number

item_cost_3 = None  # Let the user enter a number
item_count_3 = None  # Let the user enter a number

# Calculate the total
total = None
print(total)

item_cost_1 = int(input("Enter the price:"))  # Let the user enter a number
item_count_1 = int(input("Enter number of items:"))  # Let the user enter a number

item_cost_2 = int(input("Enter the price:"))  # Let the user enter a number
item_count_2 = int(input("Enter number of items:"))  # Let the user enter a number

item_cost_3 = int(input("Enter the price:"))  # Let the user enter a number
item_count_3 = int(input("Enter number of items:"))  # Let the user enter a number


total = item_cost_1 * item_count_2 + item_cost_2 * item_count_2 + item_cost_3 * item_count_3
print("My total expenses:",total)



