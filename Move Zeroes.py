"""
Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.
Note:
    You must do this in-place without making a copy of the array.
    Minimize the total number of operations.

Example:
    Input: [0,1,0,3,12]
    Output: [1,3,12,0,0]
"""


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        length = len(nums)
        i = 0
        index = 0
        while i < length:
            if nums[index] == 0:
                nums.pop(index)
                nums.append(0)
            else:
                index += 1
            i += 1

        # i = 0
        # zeros = 0
        # while i < len(nums):
        #     if nums[i] == 0:
        #         nums.pop(i)
        #         zeros += 1
        #     else:
        #         i += 1
        # nums.extend([0] * zeros)
