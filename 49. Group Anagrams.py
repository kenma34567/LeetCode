class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = {}
        sortedStrs = ["".join(sorted(s)) for s in strs]

        for i in range(len(strs)):
            sortedS = sortedStrs[i]
            anagrams[sortedS] = anagrams.get(sortedS, [])
            anagrams[sortedS].append(strs[i])

        return list(anagrams.values())
