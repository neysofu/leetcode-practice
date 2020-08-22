class NumArray:

    def __init__(self, nums):
        self.nums = nums

    def update(self, i: int, val: int) -> None:
        # constant
        # constant
        self.nums[i] = val

    def sumRange(self, i: int, j: int) -> int:
        # linear
        # log
        return sum(self.nums[i:j+1])
