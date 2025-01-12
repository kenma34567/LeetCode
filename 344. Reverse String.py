"""
Runtime: 218 ms Beats 42.19%
Memory: 18.3 MB Beats 81.18%
"""

class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        for i in range(len(s)//2):
            temp = s[i]
            s[i] = s[len(s)-1-i]
            s[len(s)-1-i] = temp
        print("S", s)
