"""
Runtime: 35 ms Beats 88.19%
Memory: 13.9 MB Beats 18.22%
"""

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:

        """
            compare each character in haystack (consider needle's length as well) with needle[0], if found, then continue comparing until needle ends
        """

        if len(haystack) < len(needle):
            return -1

        if haystack == needle:
            return 0

        ans = -1
        for i in range(len(haystack) - len(needle) + 1):
            h = haystack[i]
            for j in range(len(needle)):
                n = needle[j]
                h = haystack[i + j]
                correct = True
                if h != n:
                    correct = False
                    break
            if correct:
                ans = i
                break

        return ans
