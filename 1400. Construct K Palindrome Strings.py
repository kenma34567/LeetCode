class Solution:
    def canConstruct(self, s: str, k: int) -> bool:
        if k > len(s):
            return False

        counter = Counter(s)
        oddCount = 0
        for v in counter.values():
            oddCount += v % 2

        return oddCount <= k
