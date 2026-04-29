class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_hist = Counter(s)
        t_hist = Counter(t)

        return s_hist == t_hist
        