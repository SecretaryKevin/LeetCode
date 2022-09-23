def isPalindrome(x):
    """checks if int is palindrome returns bool"""
    return str(x) == str(x)[::-1]

isPalindrome(1234)
isPalindrome(12321)
isPalindrome(123321)