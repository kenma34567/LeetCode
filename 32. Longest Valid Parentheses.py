"""
Runtime: Beats 60.92%
Memory: Beats 54.50%
"""


class Solution:
    def longestValidParentheses(self, s: str) -> int:

        if not s:
            return 0

        stack = [-1]  # we need this to be -1 for handling perfect/leading parentheses pattern
        largestTotal = 0

        for i in range(len(s)):

            # idea: save incompleted parenthesis index into stack
            # when complete, pop the last element from the stack
            # find longest by the index

            # print("checking", s[i], i, stack)
            if s[i] == '(':
                stack.append(i)
            elif s[i] == ')':
                # if stack[-1] == '(':
                stack.pop()

                if not stack:
                    stack.append(i)  # no open parenthesis, only closing must be incomplete, add to stack
                else:
                    # print("i, stack", i, stack[-1])
                    largestTotal = max(largestTotal, (i - stack[-1]))

            # print("check", largestTotal, stack)
        return largestTotal

