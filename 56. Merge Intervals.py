class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:

        if len(intervals) < 2:
            return intervals

        intervals.sort()

        ans = []
        for i, interval in enumerate(intervals):
            if not ans:
                ans.append(interval)
                continue

            if ans[-1][1] >= interval[0]:
                ans[-1] = [ans[-1][0], max(ans[-1][1], interval[1])]
            else:
                ans.append(interval)

        return ans

