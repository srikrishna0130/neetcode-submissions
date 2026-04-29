class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # build hash map
        nums_hash = { value: key for key, value in enumerate(nums) }

        # enumerate over the array
        for i, val in enumerate(nums):
            diff = target - val
            if (diff in nums_hash and nums_hash[diff] != i):
                return sorted([i, nums_hash[diff]])
        