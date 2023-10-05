class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        if len(prices) < 2:
            return 0

        profitList = []
        for i in range(len(prices) - 1):
            profitList.append(-1 * (prices[i] - prices[i + 1]))
        print("profit list", profitList)

        """
            Detect change in profitList, add up if "changed" between +ve numbers OR reached end of list
        """

        maxProfit = 0
        positiveIndex = -1
        for i in range(len(profitList)):

            if profitList[i] > 0 and positiveIndex < 0:
                # print("update pos index", i)
                positiveIndex = i

            if positiveIndex >= 0 and (profitList[i] < 0 or i == len(profitList) - 1):
                # print("adding", positiveIndex, i)
                for j in range(positiveIndex, i + 1):
                    if profitList[j] > 0:
                        maxProfit += profitList[j]
                positiveIndex = -1  # reset

        return maxProfit
