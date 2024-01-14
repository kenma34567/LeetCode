class Solution:
    def areaOfMaxDiagonal(self, dimensions: List[List[int]]) -> int:

        maxArea = 0
        maxDiagonal = 0
        for i in range(len(dimensions)):
            l, w = dimensions[i][0], dimensions[i][1]
            area = l * w
            diagonal = math.sqrt(l * l + w * w)
            if diagonal > maxDiagonal:
                maxDiagonal = diagonal
                maxArea = area
            elif diagonal == maxDiagonal:
                maxArea = max(maxArea, area)

        return maxArea
