class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        counterRansomNote = Counter(ransomNote)
        counterMagazine = Counter(magazine)

        return counterRansomNote & counterMagazine == counterRansomNote

        """for c in magazine:
            if c not in wordCount:
                wordCount[c] = 0

            wordCount[c] += 1

        #print("cou", wordCount)

        for note in ransomNote:
            if note not in wordCount or wordCount[note] < 1:
                return False

            wordCount[note] -= 1

        return True"""