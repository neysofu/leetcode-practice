class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        elements = {}
        for (i, value) in enumerate(nums):
            if value in elements:
                return [elements[value], i]
            else:
                elements[target - value] = i
        raise ValueError