test_numbers = []

if test_numbers == []:
    print(0)
else:
    result_numbers = sum(test_numbers[::2]) * test_numbers[-1]
    print(result_numbers)
