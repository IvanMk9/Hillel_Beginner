def difference(*args):
    if not args:
        return 0
    for x in args:
        if not isinstance(x, (int, float)):
            return "Enter only integers or floats"
    return round(max(args) - min(args), 2)


assert difference(1, 2, 3) == 2, 'Test1'
assert difference(5, -5) == 10, 'Test2'
assert difference(10.2, 0.1, 3.4) == 10.1, 'Test3'
assert difference() == 0, 'Test4'
assert difference(1, "hello", 3) == "Enter only integers or floats", 'Test5'

print('OK')
