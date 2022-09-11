#   Daniel Templer
#   02/09/2022
#   program asks user for int and converts it roman numerals


def get_user_number():
    """gets the users number and makes sure its valid before passing number on to next function"""
    is_vaild = False
    while not is_vaild:
        print("="*30 + "\n")
        user_input = input("please input an int (between 1 to 3000) to convert: ")
        user_number = user_input.rstrip().lstrip()
        if user_number.isdigit():
            if 0 < int(user_number) <= 3000:
                is_vaild = True
            else:
                print("\nyour input wasnt vaild please try again\n")
        else:
            print("\nyour input wasnt vaild please try again\n")
    return int(user_number)


def converter(user_number):
    """"takes the supplied number and converts it to roman numerals"""
    roman_dictionary = {"m": ["", "M", "MM", "MMM"],
              "c": ["", "C", "CC", "CCC", "CD", "D","DC", "DCC", "DCCC", "CM "],
              "x": ["", "X", "XX", "XXX", "XL", "L","LX", "LXX", "LXXX", "XC"],
              "i": ["", "I", "II", "III", "IV", "V","VI", "VII", "VIII", "IX"]}
    thousands = roman_dictionary["m"][user_number // 1000]
    hundreds = roman_dictionary["c"][(user_number % 1000) // 100]
    tens = roman_dictionary["x"][(user_number % 100) // 10]
    ones = roman_dictionary["i"][user_number % 10]
    roman_numerals = (thousands + hundreds + tens + ones)
    return roman_numerals


def roman_numeral_display(user_number, roman_numerals):
    """prints results from convertion back to the user"""
    print("="*30 + "\n")
    print(f"you inputed the number '{user_number}' in roman numerals that would be '{roman_numerals}'")


def roman_numberals():
    """"handle running all the other funtions """
    want_to_continue = True
    while want_to_continue:
        vaild_user_input = get_user_number()
        roman_numerals = converter(vaild_user_input)
        roman_numeral_display(vaild_user_input, roman_numerals)
        print("="*30 + "\n")
        user_input = input("would you like to convert another number (y/n): ").lstrip().rstrip().lower()
        if user_input.startswith("n"):
            print("\n thank you for using the converter \n")
            want_to_continue = False

roman_numberals()
