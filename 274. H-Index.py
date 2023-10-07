class Solution:
    def hIndex(self, citations: List[int]) -> int:

        occurence = dict()

        citations.sort(reverse=True)
        print("sorted", citations)

        count = 0
        for c in citations:
            count += 1
            occurence[c] = count

        # print("dict", occurence)

        hIndex = -1
        for key, value in occurence.items():
            possibleHIndex = min(key, value)
            hIndex = max(hIndex, possibleHIndex)

        return hIndex
