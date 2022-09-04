"""
Runtime: 47 ms Beats 88.04%
Memory: 14.3 MB Beats 21.93%
bfs solution
"""

class Solution:
    def numsSameConsecDiff(self, n: int, k: int) -> List[int]:

        def bfs(result: set, ans: str):

            if len(ans) == n:
                result.add(ans)
                return

            lastDigit = int(ans[-1])

            nextDigit = k + lastDigit  # small -> large
            if nextDigit < 10:
                bfs(result, ans + str(nextDigit))

            nextDigit2 = lastDigit - k  # large -> small
            if nextDigit2 > -1:
                bfs(result, ans + str(nextDigit2))

        result = set()

        for i in range(1, 10):
            bfs(result, str(i))

        print("RES", result)
        return result
