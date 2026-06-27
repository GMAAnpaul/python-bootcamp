# TODO: Ask the user how many items will be calculated
input_count = int(input("How many items calculated:"))

total = 0

# TODO: Use a for loop to ask for more than one cost and count
for item in range(input_count):
    item_cost = int(input("How much is the cost:"))
    item_count = int(input("How many item:"))
    item_total = item_count * item_cost
    total += item_total
print("The total sales:",total)
