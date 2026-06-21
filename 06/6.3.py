input_number = int(input("Enter an integer number: "))

while input_number > 9:
    product = 1
    while input_number > 0:
        digit = input_number % 10
        product = product * digit
        input_number = input_number // 10
    input_number = product

print(input_number)