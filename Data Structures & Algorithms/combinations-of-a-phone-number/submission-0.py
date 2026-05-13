class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        digits_to_letters = {
            '2': ['a', 'b', 'c'],
            '3': ['d', 'e', 'f'],
            '4': ['g', 'h', 'i'],
            '5': ['j', 'k', 'l'],
            '6': ['m', 'n', 'o'],
            '7': ['p', 'q', 'r', 's'],
            '8': ['t', 'u', 'v'],
            '9': ['w', 'x', 'y', 'z'],
        }

        res = []
        for d in digits:
            letters = digits_to_letters[d]
            if res == []:
                res = letters
                continue
            
            temp = []
            for l in letters:
                print(l, res)
                temp = temp + [r + l for r in res]
            
            res = temp
        
        return res



        