class Solution:
    def isValid(self, s: str) -> bool:
        
        
        bracket_hash = { '}':'{', ')':'(', ']':'[' }

        isValid = True
        char_stack = []


        
        for char in s:
            if char in bracket_hash:
                if len(char_stack) < 1:
                    return False
                
                if bracket_hash[char] != char_stack[-1]:
                    return False
                
                char_stack.pop()
            else:
                char_stack.append(char)

        return char_stack == []


        