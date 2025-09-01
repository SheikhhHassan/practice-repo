# String is Pelindrome: If you sort the string in opposite manners and its same.

def str_palindrome(str):
    opposite_str = str[::-1]
    if opposite_str == str:
        return f"{str} is Palindrome"
    else:
        f"string is not Palindrome"                  
    return f"string is not Palindrome"

print(str_palindrome("cars"))
