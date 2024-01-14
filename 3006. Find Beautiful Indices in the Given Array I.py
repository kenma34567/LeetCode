class Solution:
    def beautifulIndices(self, s: str, a: str, b: str, k: int) -> List[int]:
        indexDict = {}
        for i, c in enumerate(s):
            if c == a[0] and i + len(a) - 1 <= len(s) and s[i:i + len(a)] == a:
                indexDict[a] = indexDict.get(a, [])
                indexDict[a].append(i)
            if c == b[0] and i + len(b) - 1 <= len(s) and s[i:i + len(b)] == b:
                indexDict[b] = indexDict.get(b, [])
                indexDict[b].append(i)

        if b not in indexDict or a not in indexDict:
            return []

        ans = []
        usedIndexA = set()
        for indexB in indexDict[b]:
            for indexA in indexDict[a]:
                if indexA in usedIndexA:
                    continue
                if abs(indexB - indexA) <= k:
                    ans.append(indexA)
                    usedIndexA.add(indexA)

        return ans

