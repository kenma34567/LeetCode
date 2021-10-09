"""
Runtime: Beats 55.75%
Memory: Beats 94.91%
"""


class Solution:
    def romanToInt(self, s: str) -> int:

        roman_dict = {
            "I" : 1,
            "IV": 4,
            "V" : 5,
            "IX": 9,
            "X" : 10,
            "XL": 40,
            "L" : 50,
            "XC": 90,
            "C" : 100,
            "CD": 400,
            "D" : 500,
            "CM": 900,
            "M" : 1000
        }

        pointer = 0
        ans = 0

        while pointer < len(s):

            substr = s[pointer:pointer + 2] if pointer + 1 < len(s) else s[pointer]
            if substr in roman_dict:
                ans += roman_dict[substr]
            else:
                substr = s[pointer]
                if substr in roman_dict:
                    ans += roman_dict[substr]
                else:
                    print("INVALID INPUT")
                    break
            print("substr got", substr)
            pointer += len(substr)

        return ans



