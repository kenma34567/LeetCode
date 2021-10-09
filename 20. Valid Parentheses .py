"""
Runtime: Beats 88.85%
Memory: Beats 63.34%
"""


class Solution:
    def isValid(self, s: str) -> bool:

        pairs = {
            ")": "(",
            "]": "[",
            "}": "{",
        }

        # closings = pairs.keys()
        # remove openings if input is ensured to be valid
        openings = set(pairs.values())
        stack = []
        last_p = None
        valid = True

        for i in range(len(s)):

            if s[i] in openings:
                stack.append(s[i])
            elif s[i] in pairs.keys():
                if pairs[s[i]] == last_p:
                    del stack[-1]
                else:
                    valid = False

            last_p = stack[-1] if len(stack) > 0 else None

        if len(stack) > 0:
            valid = False

        return valid





