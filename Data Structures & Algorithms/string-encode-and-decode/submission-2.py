class Solution:

    def encode(self, strs: List[str]) -> str:
        modified_strs = [ f"{len(s)}#{s}" for s in strs ]
        return "".join(modified_strs)

    def decode(self, s: str) -> List[str]:
        # parse the string, parse num

        size = 0
        strs = []
        i = 0
        j = 0

        print(s)
        while j < len(s):
            print(i,j, s[i], s[j])
            if (s[j] != '#'):
                j+=1
            else:
                size = int(s[i:j])
                strs.append(s[j+1:j+size+1])
                j = j+1+size
                i = j
        
        return strs
            
                
