class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:

        sPointer = tPointer = 0

        while sPointer < len(s) and tPointer < len(t):

            # print("comparing", s[sPointer], t[tPointer])
            if s[sPointer] == t[tPointer]:
                sPointer += 1

            tPointer += 1

        # print("check", sPointer)
        return sPointer == len(s)
