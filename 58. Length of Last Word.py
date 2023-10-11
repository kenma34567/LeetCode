class Solution:
    def lengthOfLastWord(self, s: str) -> int:

        l = 0
        s = s.strip()
        print("check", s)

        for i in range(len(s) - 1, -1, -1):
            if s[i] == ' ':
                break
            l += 1

        return l