class Solution:
    def checkValidString(self, s: str) -> bool:
        leftMin, leftMax = 0, 0

        for c in s:
            if c == "(":
                leftMin += 1
                leftMax += 1
            elif c == "*":
                leftMin = max(leftMin - 1, 0)
                leftMax += 1
            elif c == ")":
                leftMin = max(leftMin - 1, 0)
                leftMax -= 1
                if leftMax < 0:
                    return False

        print("left", leftMin, leftMax)
        return leftMin == 0

