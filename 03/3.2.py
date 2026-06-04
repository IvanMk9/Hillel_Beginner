list_numbers = [12, 3, 4, 10]

if not list_numbers:
   print(list_numbers)
else:
   list_numbers.insert(0, list_numbers[-1])
   list_numbers.pop(-1)
   print(list_numbers)