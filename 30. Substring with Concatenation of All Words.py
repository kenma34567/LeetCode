class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:

        wordDict = Counter(words)
        # print(wordDict)

        noOfWords = len(words)
        wordLength = len(words[0])
        ans = []

        for start in range(len(s) - (wordLength * noOfWords) + 1):

            wordSeen = dict()

            for count in range(noOfWords):

                left = start + count * wordLength
                right = left + wordLength
                checkString = s[left:right]
                # print("check string", checkString)

                if checkString not in wordDict:
                    break

                wordSeen[checkString] = wordSeen.get(checkString, 0) + 1

            if wordSeen == wordDict:
                ans.append(start)

        return ans
