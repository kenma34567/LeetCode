"""
Runtime: Beats 64.48%
Memory: Beats 54.63%
"""


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        common_prefix = ""
        counter = 0
        halt = False
        shortest = len(strs[0])
        for s in strs[1:len(strs)]:
            if len(s) < shortest:
                shortest = len(s)

        while counter < shortest and not halt:
            compare_char = strs[0][counter]
            for s in strs[1:len(strs)]:
                if len(s) <= counter:
                    halt = True
                    break
                if s[counter] != compare_char:
                    halt = True
                    break
            if not halt:
                common_prefix += compare_char
                counter += 1

        return common_prefix
