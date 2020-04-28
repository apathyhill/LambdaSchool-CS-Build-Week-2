# Problem:
# Contains Duplicate

# URL: 
# https://leetcode.com/problems/contains-duplicate/

# Solution:
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # Sets cannot carry duplicate values,
        # so if the length of the list is different from
        # the list converted into a set,
        # there must be at least one duplicate value.
        return len(set(nums)) < len(nums)