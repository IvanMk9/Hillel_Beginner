list_numbers = [1, 2, 3, 4, 5, 6]

split = (len(list_numbers) + 1) // 2
first_half = list_numbers[:split]
second_half = list_numbers[split:]

print([first_half, second_half])
