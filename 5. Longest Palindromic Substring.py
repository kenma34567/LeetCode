class Solution:
    def longestPalindrome(self, s: str) -> str:

        def findPalindromic(left, right):
            while left > -1 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            # last move of left and right is not palindromic
            return s[left+1:right]

        ans = s[0]
        for i in range(len(s)):
            odd = findPalindromic(i, i)
            even = findPalindromic(i, i+1)
            #print("palStr", i, odd, even)
            if len(even) > len(odd) and len(even) > len(ans):
                ans = even
            elif len(odd) > len(even) and len(odd) > len(ans):
                ans = odd

        return ans
