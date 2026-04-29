class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_dict = [ (value, index) for index, value in enumerate(nums) ]

        sorted_nums = sorted(nums_dict, key=lambda x: x[0])

        start = 0
        end = len(nums) - 1

        for i in range(len(nums)):
            if sorted_nums[start][0] + sorted_nums[end][0] == target:
                return sorted([sorted_nums[start][1], sorted_nums[end][1]])
            elif sorted_nums[start][0] + sorted_nums[end][0] > target:
                end -= 1
            else:
                start += 1
        