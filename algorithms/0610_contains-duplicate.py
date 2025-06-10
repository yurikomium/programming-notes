"""
Duplicate Detection - Final Solution
https://neetcode.io/problems/duplicate-integer?list=neetcode150

Time Complexity: O(n)
Space Complexity: O(n)
Last Updated: 2025-06-10
"""

def containsDuplicate(nums):
    seen = set() # これまでに処理した要素を覚えておく場所"seen"
    for num in nums:
        if num in seen:
            return True
        seen.add(num)
    return False