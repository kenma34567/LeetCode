class Solution:
    def reverseWords(self, s: str) -> str:
        splited = s.split()
        return " ".join(splited[::-1])
