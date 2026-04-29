class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        a = {}
        hasDuplicate = False

        for num in nums:
            if a.get(num, 0):
                hasDuplicate = True
                break
            else:
                a[num] = 1

        return hasDuplicate

         