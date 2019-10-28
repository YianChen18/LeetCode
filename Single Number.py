"""
Given a non-empty array of integers, every element appears twice except for one. Find that single one.

Note: Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?

Example 1:
    Input: [2,2,1]
    Output: 1
Example 2:
    Input: [4,1,2,1,2]
    Output: 4
"""


"""
    {} dict(table) use a lot less memory than a [] list
"""


class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # can also use [], but...
        thistable = {}
        for num in nums:
            if num in thistable:
                thistable.pop(num)
            else:
                thistable[num] = num
        return thistable.popitem()[0]
