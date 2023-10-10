class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:

        # must not have enough gas
        if sum(gas) < sum(cost):
            return -1

        tank = ans = 0

        for i in range(len(gas)):

            tank += gas[i]
            # print("i", i, tank)

            # unreachable, check next
            if tank < cost[i]:
                print("unreachable")
                tank = 0
                ans = i + 1
                continue

            tank -= cost[i]

        return ans
