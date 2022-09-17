"""
Runtime: 1758 ms Beats 85.36%
Memory: 34.3 MB Beats 11.33%
"""

class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:

        """ len of "changed" must be twice the original as every doubled element has to be appended
                if length of "changed" is odd, then must be invalid
                after that, construct a map to count elements in "changed"
                then sort "changed" in descending order
                loop through the sorted "changed" to match whether num//2 exists (ignore odd numbers)
                note: case [1,1,2] is also invalid
        """

        if len(changed) % 2 != 0:
            return []

        valueToIndexDict = dict()
        for num in changed:
            if num not in valueToIndexDict:
                valueToIndexDict[num] = 0
            valueToIndexDict[num] += 1

        print("CC", valueToIndexDict)
        original = []
        changed.sort(reverse=True)
        for num in changed:
            if num % 2 != 0:
                continue
            if num // 2 in valueToIndexDict and valueToIndexDict[num] > 0 and valueToIndexDict[num // 2] > 0:
                if num == 0 and valueToIndexDict[num] < 2:
                    continue
                original.append(num // 2)
                valueToIndexDict[num] -= 1
                valueToIndexDict[num // 2] -= 1
        print("after", valueToIndexDict)
        print("ori", original)

        if len(original) == len(changed) // 2:
            return original

        return []



