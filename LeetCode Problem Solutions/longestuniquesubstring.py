class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest_substring = 0
        seen_letters = {}
        index_of_seen = 0
        current_length = 0
        
        if s is None:
            return 0
        
        for x in range(len(s)):
            if s[x] in seen_letters and seen_letters[s[x]] >= index_of_seen: 
                
                longest_substring = max(current_length, longest_substring)
                current_length = x - seen_letters[s[x]]
                index_of_seen = seen_letters[s[x]]
                
            
            else:
                current_length += 1
                
            seen_letters[s[x]] = x
                
        longest_substring = max(current_length, longest_substring)     
                
                
        return longest_substring
            
