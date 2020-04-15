class Solution:
    def longestPalindrome(self, s: str) -> str:
        def expandFromCenter(s, left, right):
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1 #move to left
                right += 1 #move to right
            return s[left + 1: right]
  
        if s == "":
            return ""
        
        if s == s[::-1]:
            return s
        
        answer = ""
        
        for i in range(len(s)):
            odd = expandFromCenter(s, i, i)
            even = expandFromCenter(s,i, i+1)
            answer = max(answer, odd, even,key=len)
        
        
                            
        return answer
                        
                        
                    
                    
