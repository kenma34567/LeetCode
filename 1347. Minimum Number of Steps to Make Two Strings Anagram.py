class Solution:
    def minSteps(self, s: str, t: str) -> int:
        counterS, counterT = Counter(s), Counter(t)
        counterS.subtract(counterT)
        count = sum(v if v < 0 else 0 for v in counterS.values())

        return -1 * count
