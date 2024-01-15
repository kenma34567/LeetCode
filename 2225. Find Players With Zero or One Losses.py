class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        loseCountDict = dict()
        allPlayers = set()
        for m in matches:
            allPlayers.add(m[0])
            allPlayers.add(m[1])
            loseCountDict[m[1]] = loseCountDict.get(m[1], 0)
            loseCountDict[m[1]] += 1

        answer = []
        notLost, notLostHeap = [], []
        lostOne, lostOneHeap = [], []
        for p in allPlayers:
            if p not in loseCountDict:
                # heapq.heappush(notLostHeap, p)
                notLost.append(p)
        # while notLostHeap:
        # notLost.append(heapq.heappop(notLostHeap))

        for k, v in loseCountDict.items():
            if v == 1:
                # heapq.heappush(lostOneHeap, k)
                lostOne.append(k)
        # while lostOneHeap:
        # lostOne.append(heapq.heappop(lostOneHeap))
        notLost.sort()
        lostOne.sort()

        answer.append(notLost)
        answer.append(lostOne)

        return answer
