
def products( product_1, product_2, product_3=1):
    return product_1 * product_2 * product_3

input_1= int(input("Enter Product 1:"))
input_2= int(input("Enter Product 2:"))
input_3= int(input("Enter Product 3:"))
result = products(input_1, input_2, input_3)
print(result)

result = products (input_1, input_2)
print(result)