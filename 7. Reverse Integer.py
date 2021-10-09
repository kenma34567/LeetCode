"""
Runtime: Beats 76.10%
Memory: Beats 11.42%
"""


class Solution:
    def reverse(self, x: int) -> int:

        s = str(x)

        if s is None or len(s) == 0:
            return 0

        pos_limit = 0x7fffffff
        neg_limit = -0x80000000
        expected_result = None

        reversed = None

        if x >= 0:
            reversed = int(s[::-1])
            limit = pos_limit
            expected_result = reversed
        else:
            print("??", s[:0:-1])
            reversed = -1 * int(s[:0:-1])
            limit = neg_limit
            expected_result = neg_limit

        print("cal", reversed, limit)
        result = reversed & limit

        if result != expected_result:
            return 0
        elif reversed < 0:
            return reversed
        return result
