import string

user_string = input("Enter your string for hashtag: ")

clean = ''
for ch in user_string:
    if ch not in string.punctuation:
        clean += ch

hashtag = '#'
for word in clean.split():
    hashtag += word.capitalize()

hashtag = hashtag[:140]

print(hashtag)
