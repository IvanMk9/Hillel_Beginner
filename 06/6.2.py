# Текст в рядках буде українською,  а не англйською, через умову завдання про дні

seconds = int(input("Введіть кількість секунд (0 - 8639999): "))

days, remainder = divmod(seconds, 24 * 60 * 60)
hours, remainder = divmod(remainder, 60 * 60)
minutes, secs = divmod(remainder, 60)

if days % 10 == 1 and days % 100 != 11:
    day_word = "день"
elif days % 10 in (2, 3, 4) and not (11 <= days % 100 <= 14):
    day_word = "дні"
else:
    day_word = "днів"

hours_str = str(hours).zfill(2)
minutes_str = str(minutes).zfill(2)
secs_str = str(secs).zfill(2)

print(f"{days} {day_word} {hours_str}:{minutes_str}:{secs_str}")