class Solution:
    def isHappy(self, n: int) -> bool:

        def getSumOfSquares(n: int):
            ans = 0
            while n > 0:
                num = n % 10
                ans += num * num
                n = n // 10
            return ans

        ansSet = set()
        ans = n
        while ans != 1:

            ans = getSumOfSquares(ans)
            # print("ans", ans)

            if ans in ansSet:
                print("loop detected")
                return False

            ansSet.add(ans)

        return True
