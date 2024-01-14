class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:

        pendings = 0
        ans = 0
        for i in range(len(bank)):
            count = bank[i].count("1")
            if count == 0:
                continue
            ans += pendings * count
            pendings = count

        return ans
