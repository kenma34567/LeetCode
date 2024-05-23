class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:

        revisions1, revisions2 = version1.split("."), version2.split(".")
        for i in range(max(len(revisions1), len(revisions2))):
            r1, r2 = 0, 0
            if i < len(revisions1):
                r1 = int(revisions1[i])
            if i < len(revisions2):
                r2 = int(revisions2[i])
            if r1 < r2:
                return -1
            elif r1 > r2:
                return 1

        return 0
