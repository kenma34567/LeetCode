"""
Runtime: 41 ms Beats 82.22%
Memory: 13.8 MB Beats 59.17%
Dynamic Programming + greedy
"""

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        largeInteger = int(''.join(str(x) for x in digits))
        print(largeInteger)
        largeInteger += 1
        return [str(x) for x in str(largeInteger)]
