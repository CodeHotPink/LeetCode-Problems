""" 
This is the question from LeetCode:

Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:

Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
"""

example_nums = [2, 7, 11, 15]

def twoSum(nums, target):
    """ returns the two indices which sum to target """
    for indice in range(0, len(nums)):
        for second_indice in range(0, len(nums)):
            if indice == second_indice:
                pass
            else:
                if nums[indice] + nums[second_indice] == target:
                    return [indice, second_indice] 
    return False