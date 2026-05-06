class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []
        l = "("
        r = ")"

        def dfs(subset, left, right):
            if left == right == 0:
                result.append(subset)
            
            if left > right or right < 0 or left < 0 or right > n or left > n:
                return
            
            dfs(subset + l, left - 1, right)
            dfs(subset + r, left, right - 1)

        dfs("", n, n)

        return result