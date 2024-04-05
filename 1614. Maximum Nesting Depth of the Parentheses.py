class Solution:
    def maxDepth(self, s: str) -> int:
        stack = []
        maxD = 0
        for c in s:
            if c == '(':
                stack.append(c)
            elif c == ')':
                maxD = max(maxD, len(stack))
                stack.pop()

        return maxD
