class Solution:
    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        count = 0
        for i in range(len(words)):
            for j in range(i+1, len(words)):
                count += self.isSuffixPrefix(words[i], words[j])
        
        return count
    

    def isSuffixPrefix(self, s1, s2):
        if len(s1) > len(s2):
            return 0

        for i in range(len(s1)):
            if s1[i] != s2[i]:
                return 0

            # reverse
            rev = (i + 1)*-1
            if s1[rev] != s2[rev]:
                return 0
        
        return 1