class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        res = []

        count2Dict = dict()
        for w2 in words2:
            counterW2 = Counter(w2)
            for c in w2:
                count2Dict[c] = max(count2Dict.get(c, 0), counterW2[c])

        print(count2Dict)

        for w1 in words1:
            counter1 = Counter(w1)
            valid = True
            for k in count2Dict.keys():
                if counter1.get(k, 0) < count2Dict[k]:
                    valid = False
                    break
            if valid:
                res.append(w1)

        return res
