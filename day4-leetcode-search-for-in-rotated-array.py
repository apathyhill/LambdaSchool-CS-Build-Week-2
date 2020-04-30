# Problem:
# Search in Rotated Sorted Array

# URL: 
# https://leetcode.com/problems/search-in-rotated-sorted-array/

# Solution:
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if len(nums) == 0: # If list is empty, return -1
            return -1
        
        # Find pivot by finding which next is less than current element
        pivot = None
        for n in range(len(nums)-1):
            if nums[n] > nums[n+1]:
                pivot = n
                
        if pivot is None: # If no pivot, it is not rotated, so search normally
            return self.binary_search(nums, target, 0, len(nums)-1)
        
        if target >= nums[0]: # Search up to pivot if greater or equal to first element
            return self.binary_search(nums, target, 0, pivot)
        else: # Else, search from pivot to end
            return self.binary_search(nums, target, pivot+1, len(nums)-1)
        
    def binary_search(self, nums, target, low, high):
        # Basic Binary Search Code
        
        mid = (high+low) // 2 # Get midpoint index
        
        # If low and high are same index, check that value
        if low == high: 
            if target == nums[mid]:
                return mid
            else:
                return -1
        # Else, narrow down search if hadn't found result
        if target < nums[mid]:
            return self.binary_search(nums, target, low, mid)
        elif target > nums[mid]:
            return self.binary_search(nums, target, mid+1, high)
        elif target == nums[mid]:
            return mid