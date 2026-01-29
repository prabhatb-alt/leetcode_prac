# Leetcode Problem 268 - Missing Number
# Given an array containing n distinct numbers taken from 0, 1, 2, ..., n, 
# find the one that is missing from the array.

# Approach 1: Brute Force - O(n^2)
class Solution(object):
    def missingNumber(self, nums):
        n = len(nums)
        for i in range(n + 1):
            flag = False
            for num in nums: 
                if num == i:
                    flag = True
                    break

            if not flag:
                return i
            
# Time Complexity: O(n^2): Slow for larger inputs
# Space Complexity: O(1)

# Approach 2: Sorting Based - O(nlogn)
class Solution(object):
    def missingNumber(self, nums):
        nums.sort()
        for i in range(len(nums)):
            if nums[i] != i:
                return i
        return len(nums)
    
# Time Complexity: O(n log n): Due to sorting
# Space Complexity: O(1)