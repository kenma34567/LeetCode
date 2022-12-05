"""
Runtime: 102 ms Beats 36.74%
Memory: 15.3 MB Beats 43.64%
"""


class Solution:
    def frequencySort(self, s: str) -> str:
        """
        """

        lettersToFreqDict = {}
        freqToLettersDict = {}

        for c in s:
            if c not in lettersToFreqDict:
                lettersToFreqDict[c] = 0
            lettersToFreqDict[c] += 1

        # print("check", lettersToFreqDict)

        for k, v in lettersToFreqDict.items():
            if v not in freqToLettersDict:
                freqToLettersDict[v] = []
            freqToLettersDict[v].append(k)

        # print("check2", freqToLettersDict)

        # sortedKeys = sorted(freqToLettersDict.keys(), reverse=True)
        maxOccurance = len(s)

        ans = ""
        for i in range(maxOccurance, 0, -1):
            if i in freqToLettersDict:
                for j in freqToLettersDict[i]:
                    ans += ''.join(j * i)

        return ans
