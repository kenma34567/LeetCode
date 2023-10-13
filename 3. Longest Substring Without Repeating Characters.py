class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        sub = set()
        ans = 0
        left = 0

        for right in range(len(s)):

            while s[right] in sub:
                sub.remove(s[left])
                left += 1
            
            sub.add(s[right])
            ans = max(ans, right-left+1)

        return ans
