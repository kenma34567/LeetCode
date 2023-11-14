class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        countDict = dict()
        ans = 0
        maxCount = 0
        left = 0
        maxChar = s[left]
        for right, char in enumerate(s):
            countDict[char] = countDict.get(char, 0) + 1
            if countDict[char] > maxCount:
                maxChar = char
                maxCount = countDict[char]

            length = right - left + 1
            while length - maxCount > k:
                countDict[s[left]] -= 1
                if s[left] == maxChar:
                    maxCount = max(countDict.values())
                left += 1
                length = right - left + 1

            ans = max(ans, length)

        return ans
