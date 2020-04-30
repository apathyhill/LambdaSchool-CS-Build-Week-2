# Problem:
# Find the Duplicate Number

# URL: 
# https://leetcode.com/problems/find-the-duplicate-number/

# Solution:
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # Since all numbers are within 1 and the length of the list,
        # we can make the index the list at the current value and make it negative,
        # and check if it's already negative that must mean it's a duplicate value
        for num in nums:
            if nums[abs(num)] < 0:
                return abs(num)
            else:
                nums[abs(num)] = -nums[abs(num)]