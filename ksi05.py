def is_palindrome(s):
    ln = (len(s)/2) 

    for i in range(ln):
        if s[i] != s[-(i+1)]:
            return False
    return True

# Testy:
print(is_palindrome("anna")) # True
print(is_palindrome("prst")) # False
print(is_palindrome("oko")) # True
print(is_palindrome("oka")) # False

# def is_palindrome(s):
#     for i in range(len(s)):
#         if s[i] != s[len(s)-i-1]:
#             return False
#     return True