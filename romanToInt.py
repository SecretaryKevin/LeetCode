# Daniel Templer
# 09/09/2022
# converts from roman nenrals back to int
class Solution:
    def romanToInt(self, s: str) -> int:
        """converts roman to int"""
        final_int = 0
        roman_dict = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        for i in range(len(s)):
            if i > 0 and roman_dict[s[i]] > roman_dict[s[i-1]]:
                final_int += roman_dict[s[i]] -2 * roman_dict[s[i-1]]
            else:
                final_int += roman_dict[s[i]]
        return final_int

print(Solution().romanToInt("MCMXCIV"))
        
        
