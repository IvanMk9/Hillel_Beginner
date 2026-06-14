import keyword
import string

user_name = input("Enter name for variable: ")
test_result = True

if user_name[0].isdigit():
    test_result = False
elif any(upper_letters.isupper() for upper_letters in user_name):
    test_result = False
elif " " in user_name:
    test_result = False
elif "__" in user_name:
    test_result = False
elif keyword.iskeyword(user_name):
    test_result = False
else:
    forbidden = string.punctuation.replace("_", "")
    if any(x in forbidden for x in user_name):
        test_result = False

print(test_result)
