def is_even(digit):
    """ Перевірка чи є парним число """
    if not isinstance(digit, int):
        return "Enter only integer"
    if digit % 2 == 0:
        return True
    else:
        return False


assert is_even(2) == True, 'Test1'
assert is_even(5) == False, 'Test2'
assert is_even(0) == True, 'Test3'
assert is_even("hello") == "Enter only integer", 'Test4'

print('OK')
