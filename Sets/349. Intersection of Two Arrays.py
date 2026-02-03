# Problem 349: Intersection of Two Arrays
# Given two integer arrays nums1 and nums2, return an array of their intersection.
# Each element in the result must be unique and you may return the result in any order.

# Example 1:
# Input: nums1 = [1,2,2,1], nums2 = [2,2]
# Output: [2]   

# Example 2:
# Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
# Output: [9,4]
# Explanation: [4,9] is also accepted.

# Example 3:
# Input: nums1 = [1,2,3], nums2 = [4,5,6]
# Output: []

# Approach: Using Direct Set Intersection
class Solution(object):
    def intersection(self, nums1, nums2):
        return(list(set(nums1) & set(nums2)))
    
# Time Complexity: O(n + m)
# Space Complexity: O(n + m)

# Approach: Dont use direct set intersection
class Solution(object):
    def intersection(self, nums1, nums2):
        s1 = set(nums1)
        s2 = set(nums2)
        l = []
        for i in s1:
            if i in s2:
                l.append(i)
        return l

# Time Complexity: O(n + m)
# Space Complexity: O(n + m)