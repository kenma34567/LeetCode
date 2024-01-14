class Solution:
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:

        MOD = 10 ** 9 + 7
        cache = {}
        ans = 0

        def roll(remainingDice: int, tempTarget: int):

            # print("processing", remainingDice, tempTarget)
            # print("C", cache)

            if remainingDice == 0:
                return 1 if tempTarget == 0 else 0

            if (remainingDice, tempTarget) in cache:
                return cache[(remainingDice, tempTarget)]

            count = 0
            for num in range(1, k + 1):
                tempTarget -= num
                count = (count + roll(remainingDice - 1, tempTarget)) % MOD
                tempTarget += num
            # print("after", remainingDice, tempTarget, count)
            cache[(remainingDice, tempTarget)] = count

            return count

        ans = roll(n, target)

        return ans
