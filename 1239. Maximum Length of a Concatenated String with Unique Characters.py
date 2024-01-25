class Solution:
    def maxLength(self, arr: List[str]) -> int:

        charSet = set()

        def hasDup(s: str):
            sChars = set()
            for char in s:
                if char in charSet or char in sChars:
                    return True
                sChars.add(char)
            return False

        def backtrack(index: int, ans: int):
            if index >= len(arr):
                return len(charSet)

            # include arr[index]
            if not hasDup(arr[index]):
                for char in arr[index]:
                    charSet.add(char)

                ans = max(ans, backtrack(index + 1, ans))

                for char in arr[index]:
                    charSet.remove(char)

            # not include arr[index]
            return max(ans, backtrack(index + 1, ans))

        return backtrack(0, 0)
