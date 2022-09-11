class Solution:
    def intToRoman(self, num: int) -> str:
        """"takes the supplied number and converts it to roman numerals"""
        roman_dictionary = {"m": ["", "M", "MM", "MMM"],
              "c": ["", "C", "CC", "CCC", "CD", "D","DC", "DCC", "DCCC", "CM "],
              "x": ["", "X", "XX", "XXX", "XL", "L","LX", "LXX", "LXXX", "XC"],
              "i": ["", "I", "II", "III", "IV", "V","VI", "VII", "VIII", "IX"]}
        thousands = roman_dictionary["m"][num // 1000]
        hundreds = roman_dictionary["c"][(num % 1000) // 100]
        tens = roman_dictionary["x"][(num % 100) // 10]
        ones = roman_dictionary["i"][num % 10]
        roman_numerals = (thousands + hundreds + tens + ones)
        return roman_numerals.replace(" ", "")     

print(Solution().intToRoman(1994))
