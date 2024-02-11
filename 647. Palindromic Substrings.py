class Solution:
    def countSubstrings(self, s: str) -> int:

        def countPalidrome(left, right):
            count = 0
            while left in range(len(s)) and right in range(len(s)) and s[left] == s[right]:
                count += 1
                left -= 1
                right += 1

            return count

        count = 0
        for i in range(len(s)):
            odd = countPalidrome(i, i)
            even = countPalidrome(i, i + 1)

            count += odd + even

        return count