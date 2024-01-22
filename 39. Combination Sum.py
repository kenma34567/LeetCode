class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:

        def backtrack(first: int, combination: []):

            result = sum(combination)
            if result == target:
                ans.append(combination[:])
                return

            for i in range(first, len(candidates)):
                c = candidates[i]
                if result + c > target:
                    continue

                combination.append(c)
                backtrack(i, combination)
                combination.pop()

        ans = []
        backtrack(0, [])

        return ans
