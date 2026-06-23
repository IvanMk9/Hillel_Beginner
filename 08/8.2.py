def is_palindrome(text):
    changed_str = [_.lower() for _ in text if _.isalpha() or _.isdigit()]
    return changed_str == changed_str[::-1]


assert is_palindrome('A man, a plan, a canal: Panama') == True, 'Test1'
assert is_palindrome('0P') == False, 'Test2'
assert is_palindrome('a.') == True, 'Test3'
assert is_palindrome('aurora') == False, 'Test4'

print("OK")
