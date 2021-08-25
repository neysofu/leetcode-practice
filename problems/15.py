class Solution:
    def threeSum(self, nums):
        triplets = set()
        nums = sorted(nums)
        last_seen = None
        for i in range(0, len(nums)):
            desired_sum = -nums[i]
            if desired_sum < 0:
                break
            if desired_sum == last_seen:
                last_seen = desired_sum
                continue
            missing_elements = set()
            for j in range(i+1, len(nums)):
                n = nums[j]
                complement = desired_sum - n
                if n in missing_elements:
                    triplets.add((-desired_sum, n, complement))
                else:
                    missing_elements.add(complement)
        return triplets