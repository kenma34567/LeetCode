"""
Runtime: 534 ms Beats 37.89%
Memory: 16.4 MB Beats 65.31%
"""


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        ''' if "1" is found, turn all the "1"s that is connected to it recursively'''

        def islandToWater(i, j):

            ''' Turn Left, Right, Top, Bottom to "Water" recursively until all adjacent element are "0"s '''
            if j < 0 or j == len(grid[0]) or i < 0 or i == len(grid) or grid[i][j] == "0":
                return
            grid[i][j] = "0"

            islandToWater(i, j - 1)  # Left
            islandToWater(i, j + 1)  # Right
            islandToWater(i - 1, j)  # Top
            islandToWater(i + 1, j)  # Bottom

        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):  # same for each line

                current = grid[i][j]
                if current == "1":
                    count += 1
                    islandToWater(i, j)

        return count
