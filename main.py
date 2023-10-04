from typing import List


def twoSum(self, nums: List[int], target: int) -> List[int]:
    index = {}

    for i, num in enumerate(nums):
        operand = target - num
        if operand in index:
            return [index[operand], i]
        index[num] = i

    return index
