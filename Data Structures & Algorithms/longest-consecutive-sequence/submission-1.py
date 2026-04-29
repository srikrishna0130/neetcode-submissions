class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_hash = defaultdict(list)

        if (len(nums) == 0):
            return 0

        for i in nums:
            print(i, num_hash)
            if (i in num_hash):
                continue
            else:
                num_hash[i] = [i,i]

            if ((i-1 in num_hash) & (i+1 not in num_hash)):
                num_hash[i] = num_hash[i-1]
                num_hash[i-1][1] = i
                continue
            
            if ((i-1 not in num_hash) & (i+1 in num_hash)):
                num_hash[i] = num_hash[i+1]
                num_hash[i+1][0] = i
                continue
            
            if ((i-1 in num_hash) & (i+1 in num_hash)):
                num_hash[i-1][1] = num_hash[i+1][1]
                num_hash[i+1] = num_hash[i-1]
                num_hash[i] = num_hash[i+1]
                continue
            
        counts = [val[1]-val[0]+1 for val in num_hash.values()]
        return max(counts)

        