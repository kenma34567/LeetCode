class Solution:
    def flowerGame(self, n: int, m: int) -> int:
        ans = 0
        oddN = n // 2 if n % 2 == 0 else n // 2 + 1
        oddM = m // 2 if m % 2 == 0 else m // 2 + 1
        evenN = n - oddN
        evenM = m - oddM
        print("C", oddN, oddM)

        return oddN * evenM + evenN * oddM
