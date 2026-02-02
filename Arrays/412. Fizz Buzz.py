# Problem 412: Fizz Buzz
# Given an integer n, return a string array answer (1-indexed) where:
# answer[i] == "FizzBuzz" if i is divisible by 3 and 5.
# answer[i] == "Fizz" if i is divisible by 3.
# answer[i] == "Buzz" if i is divisible by 5.
# answer[i] == i (as a string) if none of the above conditions are true.

"""
# Approach: Iteration - O(n)
class Solution(object):
    def fizzBuzz(self, n):
        res = []
        for i in range(1, n+1):
            if i % 3 == 0 and i % 5 == 0:
                res.append("FizzBuzz")
            elif i % 3 == 0:
                res.append("Fizz")
            elif i % 5 == 0:
                res.append("Buzz")
            else:
                res.append(str(i))
        
        return res
    
sol = Solution()
print(sol.fizzBuzz(15))
# Time Complexity: O(n)
# Space Complexity: O(1)
"""

# Approach 2: Hash Map - O(n)
class Solution(object):
    def fizzBuzz(self, n):
        res = []
        hmap = {3: "Fizz", 5: "Buzz"}
        for i in range(1, n+1):
            s = ""
            for j in hmap:
                if i % j == 0:
                    s += hmap[j]
            if s == "":
                s = str(i)
            res.append(s)
        return res
    
sol = Solution()
print(sol.fizzBuzz(15))