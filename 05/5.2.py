while True:
    user_number_1 = input("Enter first number: ")
    if not user_number_1.isdigit():
        print("Invalid operation, use only numbers for math operations")
        exit()
    user_number_2 = input("Enter second number: ")
    if not user_number_2.isdigit():
        print("Invalid operation, use only numbers for math operations")
        exit()
    user_operation_type = input("Enter operation type (+, -, *, /): ")

    if user_operation_type == "+":
        print("Result:", int(user_number_1) + int(user_number_2))
    elif user_operation_type == "-":
        print("Result:", int(user_number_1) - int(user_number_2))
    elif user_operation_type == "*":
        print("Result:", int(user_number_1) * int(user_number_2))
    elif user_operation_type == "/":
        if user_operation_type == "/" and int(user_number_2) == 0:
            print("You can't divide by 0,  enter another number")
        else:
            print("Result:", int(user_number_1) / int(user_number_2))
    else:
         print("Invalid operation, try again")

    request = input("Do you want to continue? (yes/y - continue, any other command - exit): ")
    if request.strip().lower() not in ('yes', 'y'):
        print("Exiting...")
        break