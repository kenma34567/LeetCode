class Solution:
    def getRow(self, rowIndex: int) -> List[int]:

        ansRow = []

        for i in range(rowIndex + 1):
            row = [1] * (i + 1)
            for j in range(1, i):
                row[j] = ansRow[j - 1] + ansRow[j]
            ansRow = row

        return ansRow
