from enum import Enum


class Solution:
    def convert(self, s: str, numRows: int) -> str:

        rows = [''] * numRows
        direction, currentRow = 1, 0    # 1: go downwards, -1 go upwards

        for char in s:
            rows[currentRow] += char
            if currentRow == numRows-1:
                direction = -1
            elif currentRow == 0:
                direction = 1
            currentRow += direction
            if currentRow < 0:
                currentRow = 0
        
        return "".join(rows)
