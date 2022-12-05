"""
Runtime: 1361 ms Beats 5.02%
Memory: 15.1 MB Beats 90.84%
"""


class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        """
            First put all letters into a letter-to-count dict for word1 and word2
            Swap the dicts to become count-to-letter dicts
            Match number of chars under each "count", if same, then they are Close
        """
        if len(word1) != len(word2):
            return False

        def constructWordCountDict(word: str):

            countDict = {}

            for i in range(len(word)):
                if word[i] not in countDict:
                    countDict[word[i]] = 0
                countDict[word[i]] += 1

            return countDict

        word1CountDict = constructWordCountDict(word1)
        word2CountDict = constructWordCountDict(word2)
        # print("CHECK", word1CountDict, word2CountDict)

        if word1CountDict.keys() != word2CountDict.keys():
            return False

        def swapDict(countDict: dict):

            letterToCountDict = {}
            for k, v in countDict.items():
                if v not in letterToCountDict:
                    letterToCountDict[v] = []
                letterToCountDict[v].append(k)

            return letterToCountDict

        word1LetterToCountDict = swapDict(word1CountDict)
        word2LetterToCountDict = swapDict(word2CountDict)
        # print("swap", word1LetterToCountDict, word2LetterToCountDict)

        if word1LetterToCountDict.keys() != word2LetterToCountDict.keys():
            return False

        for k in word1LetterToCountDict:
            if len(word1LetterToCountDict[k]) != len(word2LetterToCountDict[k]):
                return False

        return True
