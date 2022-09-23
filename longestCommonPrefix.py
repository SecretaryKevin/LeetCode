def longestCommonPrefix(strs):
    """finds longest prefix shared between strings in a list"""
    longest_prefix = ""
    if len(strs) == 0: 
        return longest_prefix
    elif len(strs) == 1:
        return strs[0]
    else:
        for letter in strs[0]:
            longest_prefix = longest_prefix + letter
            for word in strs:
                if not word.startswith(longest_prefix):
                    return longest_prefix[:-1]
        return longest_prefix
        
        

    
# test data
# test one expected output "fl"
strs = ["dog","racecar","car"]
print(longestCommonPrefix(strs))
print("=*"*30)
#test two expected output ""
strs = ["flower","flow","flight"]
print(longestCommonPrefix(strs))
