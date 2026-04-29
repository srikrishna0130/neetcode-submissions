class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        if (len(nums) < 3):
            return []
        
        arr_len = len(nums)
        sorted_nums = sorted(nums)
        results = []

        for i in range(0, arr_len - 1):
            if (sorted_nums[i] > 0):
                continue

            # ignore duplicate num
            if (i > 0 and sorted_nums[i-1] == sorted_nums[i]):
                continue

            # solve the 2 sum problem
            j = i + 1
            k = arr_len - 1
            while j < k:
                # print(i, j, k)
                three_sum = sorted_nums[i] + sorted_nums[j] + sorted_nums[k]
                if three_sum > 0:
                    k -= 1
                elif three_sum < 0:
                    j += 1
                else:
                    results.append([sorted_nums[i], sorted_nums[j], sorted_nums[k]])
                    j += 1
                    k -= 1
                    while (j < k and sorted_nums[j] == sorted_nums[j-1]):
                        j += 1
                    
                    while (j < k and sorted_nums[k] == sorted_nums[k+1]):
                        k -= 1
                       
        return results

        