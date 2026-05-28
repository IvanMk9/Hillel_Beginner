# Task №1
user_number = int(input("Enter a number: "))
print("Squared number: ", user_number ** 2)

# Task №2
first_user_number = int(input("Enter the first number: "))
second_user_number = int(input("Enter the second number: "))
third_user_number = int(input("Enter the third number: "))
print("Average number: ", (first_user_number + second_user_number + third_user_number) / 3)

# Task №3
user_minutes = int(input("Enter amount of minutes: "))
print((user_minutes // 60), "hours", (user_minutes % 60), "minutes")

# Task №4
user_price = int(input("Enter price: "))
user_discount = int(input("Enter discount rate (%): "))
print("Price, including discount: ", user_price * (1 - user_discount / 100))

#Task №5
user_whole_number = int(input("Enter a whole number: "))
print("Last number: ", user_whole_number % 10)

# Task №6
user_width = int(input('Enter width: '))
user_length = int(input('Enter length: '))
print("Perimeter: ", (user_width + user_length) * 2)

# Task №7
user_4_digit_number = int(input("Enter four-digit number: "))
print(user_4_digit_number // 1000)
print((user_4_digit_number // 100) % 10)
print((user_4_digit_number // 10) % 10)
print((user_4_digit_number // 1) % 10)
