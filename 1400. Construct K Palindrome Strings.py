class Solution:
    def canConstruct(self, s: str, k: int) -> bool:
        if k > len(s):
            return False

        counter = Counter(s)
        oddCount = 0
        for v in counter.values():
            if v % 2 != 0:
                oddCount += 1
                if oddCount > k:
                    return False

        return True
