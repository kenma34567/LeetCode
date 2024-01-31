class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack, ans = [], [0] * len(temperatures)
        for i, t in enumerate(temperatures):
            while stack and t > stack[-1][1]:
                index, temp = stack.pop()
                ans[index] = i - index
            stack.append((i, t))

        # print("ans", ans)
        return ans
