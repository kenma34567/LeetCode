class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # if len(cost) < 3:
        #   return min(cost[0], cost[1])

        prevMinCost1, prevMinCost2 = cost[-2], cost[-1]

        for i in range(len(cost) - 3, -1, -1):
            current = cost[i] + min(prevMinCost1, prevMinCost2)
            prevMinCost2 = prevMinCost1
            prevMinCost1 = current

        return min(prevMinCost1, prevMinCost2)
