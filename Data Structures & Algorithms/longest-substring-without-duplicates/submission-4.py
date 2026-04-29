class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_map = {} # Maps char -> its last seen index
        left = 0
        max_length = 0
        
        for right in range(len(s)):
            # If the char is in the dict AND inside our current window
            if s[right] in char_map and char_map[s[right]] >= left:
                # Jump left pointer to one past the last occurrence
                left = char_map[s[right]] + 1
            
            # Update the last seen index of the character
            char_map[s[right]] = right
            
            # Calculate window size: (right - left + 1)
            max_length = max(max_length, right - left + 1)
            
        return max_length