class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        '''
            Best case scenario: sum(candies) // k
            For each in sum(candies) // k -> check if it is possible to divide to k piles
                --> Binary Search to reduce time\
        '''

        def checkPossible(num):
            piles = 0
            for c in candies:
                piles += c // num

            return piles >= k

        left, right = 1, sum(candies) // k
        result = 0

        while left <= right:
            mid = (left + right) // 2
            if checkPossible(mid):
                result = max(result, mid)
                left = mid + 1
            else:
                right = mid - 1

        return result
