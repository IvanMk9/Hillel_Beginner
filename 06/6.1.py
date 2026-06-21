import string

user_input = input("Enter two letters hyphenated, for example, a-c: ")

first_letter, second_letter = user_input.split("-")
first_index = string.ascii_letters.index(first_letter)
second_index = string.ascii_letters.index(second_letter)
result = string.ascii_letters[first_index:second_index + 1]

print(result)