class Solution:
    def increasingTriplet(self, nums):
        """returns true if any 3 are in increasing order in list"""
        first = second = float('inf')
        for n in nums:
            if n <= first:
                first = n
            elif n <= second:
                second = n
            else:
                return True
        return False

nums = [20,100,10,12,5,13]
print(Solution().increasingTriplet(nums))

nums = [1,2,1,3]
print(Solution().increasingTriplet(nums))

nums = [1,2,3,4,5,6]
print(Solution().increasingTriplet(nums))
