class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        def backtrack(first: int, combination: list):

            if len(combination) == k:
                # print("adding", combination)
                ans.append(combination[:])
                return

            for num in range(first, n + 1):
                combination.append(num)

                backtrack(num + 1, combination)

                combination.pop()

            return

        ans = []
        backtrack(1, [])
        return ans
