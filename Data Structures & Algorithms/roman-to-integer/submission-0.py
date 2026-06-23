class Solution:
    def romanToInt(self, s: str) -> int:
        sum_to_num = {
            "I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000,
            "IV": 4, "IX": 9, "XL": 40, "XC": 90, "CD": 400, "CM": 900
        }

        res = 0
        i = 0
        n = len(s)

        while i < n:
            # Look ahead to see if a 2-character pair can be formed
            if i + 1 < n and s[i:i+2] in sum_to_num:
                res += sum_to_num[s[i:i+2]]
                i += 2  # Skip both characters
            else:
                res += sum_to_num[s[i]]
                i += 1  # Move to the next single character
                
        return res