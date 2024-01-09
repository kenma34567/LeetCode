class Solution:
    def generate(self, numRows: int) -> List[List[int]]:

        ans = []

        for i in range(1, numRows + 1):
            row = [1] * i
            if i < 3:
                ans.append(row)
                continue

            for j in range(1, i - 1):
                prev = ans[i - 2]
                row[j] = prev[j - 1] + prev[j]
            ans.append(row)

        return ans
