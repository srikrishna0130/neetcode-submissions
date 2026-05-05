class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []

        for n in nums:
            result = self.addToResult(n, result)
        
        return result

    def addToResult(self, n, result):
        curr_result = []
        if result == []:
            curr_result.append([n])
            return curr_result

        for ele in result:
          print("element in result", ele)
          curr = []
          for i in range(len(ele) + 1):
            curr = ele[:i] + [n] + ele[i:]
            curr_result.append(curr)  
        
        return curr_result

        