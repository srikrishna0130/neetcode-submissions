class Solution:
    def partition(self, s: str) -> List[List[str]]:
        # for each partition, check take or not take

        result = []
        curr_list = []

        def dfs(i):
            if i == len(s):
                if self.isPalin(curr_list[-1]):
                    result.append(curr_list.copy())
                return 
            
            if i == 0:
                curr_list.append(s[i])
                dfs(i+1)
                curr_list.pop()
                return
            
            # split, handles i = 0 case also
            next_word = s[i]
            print(i, curr_list, next_word)
            if  self.isPalin(curr_list[-1]):
                curr_list.append(next_word)
                dfs(i+1)
                curr_list.pop()
            
            # join word case
            original_word = curr_list[-1]
            curr_list[-1] = curr_list[-1] + next_word
            dfs(i+1)
            curr_list[-1] = original_word

        
        dfs(0)

        return result
    
    def isPalin(self, word):
        return word == word[::-1]