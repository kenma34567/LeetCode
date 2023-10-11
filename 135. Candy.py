class Solution:
    def candy(self, ratings: List[int]) -> int:

        """
            @param candyDis -> distribution of candies, init: [1 * len(ratings)

            go through the array in-order and reverse-order,
            so that it can compare to the right and left neighbour respectively in each run

            [1, 0, 2]
            candyDis: [1, 1, 1]

            1st loop:   1) rating[0] > rating[1] --> candyDis: [2, 1, 1]
                        2) rating[1] < rating[2] --> candyDis: [2, 1, 1]
                        3) rating[2] has nth to compare --> candyDis: [2, 1, 1]

            2nd loop:
                        1) rating[2] > rating[1] --> candyDis: [2, 1, 2]
                        2) rating[1] < rating[0] --> candyDis: [2, 1, 2]
                        3) rating[0] has nth to compare --> candyDis: [2, 1, 2]

            return sum(candyDis)
        """

        candyDis = [1] * len(ratings)

        for i in range(1, len(ratings)):
            if ratings[i] > ratings[i - 1]:
                candyDis[i] = candyDis[i - 1] + 1

        # print("can after 1st", candyDis)

        for i in range(len(ratings) - 2, -1, -1):
            if ratings[i] > ratings[i + 1]:
                candyDis[i] = max(candyDis[i], candyDis[i + 1] + 1)

        # print("can", candyDis)

        return sum(candyDis)
