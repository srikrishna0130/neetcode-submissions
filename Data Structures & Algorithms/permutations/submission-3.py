class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = [[]]

        for n in nums:
            curr_perm = []
            for element in result:
                # n + 1 ways to insert
                for i in range(len(element)+1):
                    curr_perm.append(element[:i] + [n] + element[i:])
                result = curr_perm

        return result
        