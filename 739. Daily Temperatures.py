class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack, ans = [], [0] * len(temperatures)
        for i, t in enumerate(temperatures):
            if not stack:
                stack.append((i, t))
                continue
            index, temp = stack[-1][0], stack[-1][1]
            while t > temp:
                stack.pop()
                ans[index] = i - index
                if not stack:
                    break
                index, temp = stack[-1][0], stack[-1][1]
            stack.append((i, t))

        # print("ans", ans)
        return ans
