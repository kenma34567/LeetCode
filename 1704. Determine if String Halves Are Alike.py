class Solution:
    def halvesAreAlike(self, s: str) -> bool:

        vowels = set(['a', 'e', 'i', 'o', 'u'])
        s = s.lower()

        count = 0
        for i in range(len(s)//2):
            if s[i] in vowels:
                count += 1

        for i in range(len(s)//2, len(s)):
            if s[i] in vowels:
                count -= 1

        return count == 0
