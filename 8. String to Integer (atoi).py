"""
Runtime: Beats 98.99%
Memory: Beats 55.85%
"""


class Solution:
    def myAtoi(self, s: str) -> int:

        if s is None or len(s) == 0:
            return 0

        s = s.lstrip()

        if s is None or len(s) == 0:
            return 0

        pos_limit = 0x7FFFFFFF
        neg_limit = -0x80000000

        limit = pos_limit
        negative = s[0] is '-'

        symbol_start = False

        if s[0] is "+" or s[0] is "-":
            symbol_start = True

        num_array = []
        digit_started = False
        for i in range(len(s)):

            if s[i].isdigit():
                digit_started = True
                num_array.append(s[i])
            elif digit_started:
                # num exist, char after num
                break
            elif (symbol_start and i > 0) or not symbol_start:
                # num not exist, s[0] = +, s[1] = -
                num_array.append("0")
                negative = False
                break

        if len(num_array) == 0:
            return 0

        num = int(''.join(num_array))
        expected_value = num

        if negative:
            num *= -1
            if num < 0:
                limit = neg_limit
                expected_value = neg_limit

        print("num", num, s, expected_value, num & limit)

        if num & limit == expected_value:
            return num
        else:
            return limit



