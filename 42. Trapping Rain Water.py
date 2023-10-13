class Solution:
    def trap(self, height: List[int]) -> int:

        """
            1) Loop through the list, find the max left and max right of each position
            2) Get min(maxLeft, maxRight) of each position
            3) max(0, min(maxLeft, maxRight) - height[i]) = water that can be trapped (ignoring -ve number)
        """

        maxLeftList, maxRightList = [0] * len(height), [0] * len(height)
        maxLeft, maxRight = 0, 0
        ans = 0

        for i in range(len(height)):
            maxLeftList[i] = maxLeft
            maxLeft = max(maxLeft, height[i])
        # print("left list", maxLeftList, maxRight)

        for i in range(len(height) - 1, -1, -1):
            maxRightList[i] = maxRight
            maxRight = max(maxRight, height[i])
        # print("right list", maxRightList)

        for i in range(len(height)):
            ans += max(0, min(maxLeftList[i], maxRightList[i]) - height[i])

        return ans
