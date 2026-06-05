test_list = [0, 1, 0, 12, 3]

zero = 0
zero_count = 0

while zero < len(test_list) - zero_count:
    if test_list[zero] == 0:
        test_list.pop(zero)
        test_list.append(0)
        zero_count += 1
    else:
        zero += 1

print(test_list)
