# Price notification template
price_notification = "The price of {} is ${}."


# TODO: Post: Latte ($3.5)
new_price_notification = price_notification.format("Latte", 3.5)
print(new_price_notification)

# TODO: Post: Espresso ($2.75)
new_price_notification = price_notification.format("Espresso", 2.75)
print(new_price_notification)

# TODO: Post: Cappuccino ($4.0)
new_price_notification = price_notification.format("Cappucino", 4.0)
print(new_price_notification)


print (f"The price of {name} is ${price}.")