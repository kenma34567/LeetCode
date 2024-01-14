class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:

        time = 0
        left, right = 0, 0

        while left < len(colors):

            right += 1
            if colors[right] == colors[right - 1]:
                left = right - 1
                # print("same detected", left, right)
                while right < len(colors) and colors[right] == colors[right - 1]:
                    right += 1
                sameList = neededTime[left:right]
                # print("sameList", left, right)
                time += sum(sameList) - max(sameList)
                # print("time updated", time)

            if right >= len(colors) - 1:
                break

        return time
