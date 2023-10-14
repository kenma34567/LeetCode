class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False

        wordDict = dict()
        usedTChar = set()

        for i in range(len(s)):

            if s[i] in wordDict and wordDict[s[i]] != t[i]:
                return False

            if s[i] not in wordDict and t[i] in usedTChar:
                return False

            wordDict[s[i]] = t[i]
            usedTChar.add(t[i])

        return True
