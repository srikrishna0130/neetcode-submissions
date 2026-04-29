class Solution:
    def isPalindrome(self, s: str) -> bool:
        transformed_string = "".join(list(filter(lambda x: x.isalnum(), s.upper())))
        s_len = len(transformed_string)

        for i in range(0, s_len//2):
            if (transformed_string[i] != transformed_string[s_len - 1 - i]):
                return False

        return True

        