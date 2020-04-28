# Problem:
# Two Sum

# URL: 
# https://leetcode.com/problems/two-sum/

# Solution:
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        diffs = {} # Keep track of previous numbers
        for i, val in enumerate(nums):
            diff = target - val # Calculate difference of target value and current value
            if diff in diffs: # If the difference is in dict, taht means two values add up to the target; return both indices
                return [diffs[diff], i]
            else:
                diffs[val] = i # Add current value and index to dict 