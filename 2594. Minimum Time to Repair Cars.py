class Solution:
    def repairCars(self, ranks: List[int], cars: int) -> int:
        '''
            1 -> min(ranks)*cars^2
                -> search range, right = max time needed (do not have to consider max(ranks))

            r*n^2 = time
            -> n = sqrt(time/r)
            -> for each rank, sum up and see if the sum >= cars
                -> if yes, move right boundary and test a smaller number
                -> if no, move left boundary and test a larger number
        '''

        def canRepair(time):
            totalCars = 0
            for r in ranks:
                n = math.floor(math.sqrt(time / r))
                #print(r, "repairing", n)
                totalCars += n

            return totalCars >= cars

        left, right = 1, min(ranks) * cars * cars
        while left < right:
            mid = (left+right) // 2

            if canRepair(mid):
                right = mid
            else:
                left = mid+1

        return right
