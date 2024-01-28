class Solution:
    def maximumLength(self, nums: List[int]) -> int:
        counterN = Counter(nums)

        # print("C", counterN)

        def handleSpecialOne():
            oneCount = counterN.get(1, 0)
            if oneCount == 0:
                return 1
            return oneCount if oneCount % 2 != 0 else oneCount - 1

        def decrePopCounter(num: int, counterN: Counter):
            if num in counterN:
                counterN[num] -= 1
            if counterN[num] == 0:
                counterN.pop(num)

            return counterN

        def dfs(power: int, subset: List[int], prevCounter: int, counterN: Counter):
            if len(subset) > 1 and subset[0] == subset[-1]:
                # print("ans?", subset)
                return len(subset) if len(subset) % 2 != 0 else 1

            num = subset[0]
            t1 = num ** (2 ** power)
            t2 = subset[prevCounter]
            # print("T", num, 2**power, t1, t2, prevCounter)
            ans = 1
            if t1 in counterN:
                subsetCopy = subset.copy()
                subsetCopy.append(t1)
                # print("appended t1", subsetCopy)
                counterNCopy = decrePopCounter(t1, counterN.copy())
                ans = max(ans, dfs(power + 1, subsetCopy, prevCounter + 1, counterNCopy))
            if t2 != subset[-1] and t2 in counterN:
                subsetCopy = subset.copy()
                subsetCopy.append(t2)
                # print("appended t2", subsetCopy)
                counterNCopy = decrePopCounter(t2, counterN.copy())
                ans = max(ans, dfs(power, subsetCopy, prevCounter - 1, counterNCopy))

            return ans

        checked = set()
        ans = handleSpecialOne()
        for n in nums:
            if n in checked:
                continue
            subset = [n]
            counterNCopy = decrePopCounter(n, counterN.copy())
            ans = max(ans, dfs(1, subset, -1, counterNCopy))
            checked.add(n)

        return ans
