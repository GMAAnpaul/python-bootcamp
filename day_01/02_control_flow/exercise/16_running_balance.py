total = 5
running = True
while running:
    command = input("Provide command: ")

    if command == "add":
        Number1 = int(input("Enter number:"))
        total = total + Number1
        print(total)
        pass
    if command == "sub":
        Number2 = int(input("Enter number:"))
        total = total - Number2
        print(total)
        pass
    elif command == "exit":
        running = False
