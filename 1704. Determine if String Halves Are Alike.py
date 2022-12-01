"""
Runtime: 49 ms Beats 76.88%
Memory: 13.9 MB Beats 77.72%
"""

class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        vowelsSet = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
        mid = len(s) // 2
        firstHalf = s[:mid]
        secondHalf = s[mid:]

        count = 0
        for s in firstHalf:
            if s in vowelsSet:
                count += 1

        for s in secondHalf:
            if s in vowelsSet:
                count -= 1

        return count == 0


