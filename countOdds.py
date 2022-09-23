def countOdds(low, high):
    """counts number of odd numbers between 2 numbers"""
    N = (high - low) // 2
    if (high % 2 != 0 or low % 2 != 0):
        N += 1
    return N



print(countOdds(3,7))
print(countOdds(8,10))
print(countOdds())
    
