"""
Runtime: Beats 13.43%
Memory: Beats 24.45%
"""


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        length = 0

        for i in range(len(s)):
            char_set = set()
            temp_length = 0
            for j in range(i, len(s)):
                if not s[j] in char_set:
                    char_set.add(s[j])
                    temp_length += 1
                else:
                    break
            if temp_length > length:
                length = temp_length

        return length

