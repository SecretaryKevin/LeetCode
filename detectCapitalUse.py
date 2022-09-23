def detectCapitalUse(word):
    """detects if capital are used correctly according to question 520 leetcode"""
    if any([word == word.upper(), word == word.lower(), word == word.title()]):
        is_vaild = True
    else:
        is_vaild = False
    return is_vaild
