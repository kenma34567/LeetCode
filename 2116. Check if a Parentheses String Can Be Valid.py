class Solution:
    def canBeValid(self, s: str, locked: str) -> bool:

        lockedStack = []
        freeStack = []

        for i in range(len(s)):
            if locked[i] == "0":
                freeStack.append(i)
            elif s[i] == "(":
                lockedStack.append(i)
            else:
                if lockedStack and lockedStack[-1] < i:
                    lockedStack.pop()
                elif freeStack and freeStack[-1] < i:
                    freeStack.pop()
                else:
                    return False

        while lockedStack and freeStack and lockedStack[-1] < freeStack[-1]:
            lockedStack.pop()
            freeStack.pop()

        return len(lockedStack) == 0 and len(freeStack) % 2 == 0
