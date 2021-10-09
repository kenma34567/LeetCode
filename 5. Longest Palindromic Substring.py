"""
Runtime: Beats 47.37%
Memory: Beats 93.32%
"""


class Solution:
    def find_palindrome(self, s, start, end):

        l, r = 0, 0
        while start >= 0 and end < len(s) and s[start] == s[end]:
            # print("match!", start, end)
            if r - l < end - start:
                # print("replacing!", start, end)
                l = start
                r = end
            start -= 1
            end += 1

        return l, r

    def longestPalindrome(self, s: str) -> str:

        l = 0
        r = 0
        for i in range(len(s)):

            # print("comparing", start, end)
            l1, r1 = self.find_palindrome(s, i - 1, i + 1)
            l2, r2 = self.find_palindrome(s, i, i + 1)
            # print("!!", l2, r2, l1, r1, l, r)
            if r2 - l2 > r - l:
                l, r = l2, r2
            elif r1 - l1 > r - l:
                l, r = l1, r1

        # print(l, r)
        print(s[l:r + 1])
        return s[l:r + 1]
