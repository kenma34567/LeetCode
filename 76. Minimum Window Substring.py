class Solution:
    def minWindow(self, s: str, t: str) -> str:

        # construct a dict for counting char in t
        neededCounter = Counter(t)
        print("neededCounter", neededCounter)

        neededNum = len(t)

        # compare neededCounter vs haveCounter to see if total number of each char can satisfy
        haveCounter = Counter(s)
        # if haveCounter & neededCounter != neededCounter:
        # return ""

        haveNum = 0

        # initialize answer as full list
        ansLeft, ansRight, ansLength = -1, -1, float("inf")

        right = -1
        haveCounter = Counter()

        for left in range(len(s)):

            # move left pointer, if haveCounter[s[left-1]] becomes less than needed, haveNum -= 1
            if left > 0 and s[left - 1] in haveCounter:
                haveCounter[s[left - 1]] -= 1
                if haveCounter[s[left - 1]] < neededCounter[s[left - 1]]:
                    haveNum -= 1

            # start of the minimum window must be targeted char
            if s[left] not in neededCounter:
                continue

            while right < len(s) - 1 and haveNum < neededNum:
                right += 1
                char = s[right]
                if char not in neededCounter:
                    continue

                haveCounter[char] = haveCounter.get(char, 0) + 1
                if haveCounter[char] <= neededCounter[char]:
                    haveNum += 1
                # print("checking 2", s[left:right+1], haveCounter, haveNum)

            # print("haveCounter", haveCounter, neededCounter, neededCounter & haveCounter)
            if haveNum == neededNum and right - left + 1 < ansLength:
                # print("updating", left, right)
                ansLeft = left
                ansRight = right
                ansLength = ansRight - ansLeft + 1

        print("ansRig", ansLeft, ansRight)
        return s[ansLeft:ansRight + 1] if ansLength != float("inf") else ""
