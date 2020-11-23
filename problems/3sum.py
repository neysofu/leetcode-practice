class Solution:
    def threeSum(self, nums):
        triplets = []
        for i in range(0, len(nums)):
            for j in range(i+1, len(nums)):
                for k in range(j+1, len(nums)):
                    arr = sorted([nums[i], nums[j], nums[k]])
                    if sum(arr) == 0 and arr not in triplets:
                        triplets.append(arr)
        return triplets
