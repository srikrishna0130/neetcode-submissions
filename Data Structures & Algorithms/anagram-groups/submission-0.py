class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        # group anagrams
        grouped_strs = defaultdict(list)
        for string in strs:
            # print(string)
            grouped_strs["".join(sorted(string))].append(string)

        
        return [ value for key, value in grouped_strs.items() ]
        # return []

        