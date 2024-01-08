"""


There are n children standing in a line. Each child is assigned a rating value given in the integer array ratings.

You are giving candies to these children subjected to the following requirements:

Each child must have at least one candy.
Children with a higher rating get more candies than their neighbors.
Return the minimum number of candies you need to have to distribute the candies to the children.


"""


class Solution:

    def test(self):

        tests = [[1, 0, 2],
                 [1, 2, 2],
                 [1, 1, 1],
                 [2, 2, 2],
                 [8, 3, 4, 5, 6, 8, 7],
                 [1, 3, 2, 2, 1]]
        for t in tests:
            print("running", t)
            print("ans", self.solve(ratings=t))
            print("")

    @staticmethod
    def solve(ratings) -> int:

        candies = [1] * len(ratings)

        for i in range(1, len(ratings)):
            if ratings[i] > ratings[i-1]:
                candies[i] = candies[i-1]+1

        print("---first run", candies)

        for i in range(len(ratings)-2, -1, -1):
            if ratings[i] > ratings[i+1]:
                candies[i] = max(candies[i], candies[i+1]+1)

        print("---second run", candies)

        return sum(candies)


s = Solution()
s.test()
