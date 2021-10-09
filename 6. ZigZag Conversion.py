"""
Runtime: Beats 9.41%
Memory: Beats 12.93%
"""


class Solution:
    def convert(self, s: str, numRows: int) -> str:

        seq = [[]]
        count = len(s)

        mode = "straight"  # straight -> oblique -> straight

        straight_count = 0
        oblique_count = 0

        for i in range(numRows):
            seq.append([])

        while count > 0:

            char_index = len(s) - count
            print("doing", char_index, s[char_index])

            if mode is "straight":
                straight_index = straight_count
                print("straight_indeX", straight_index)
                seq[straight_index].append(s[char_index])
                straight_count += 1
                if straight_count >= numRows:
                    mode = "oblique"
                    straight_count = 0
            elif mode is "oblique":
                oblique_index = numRows - oblique_count - 1 - 1
                # do not consider the corner as part of oblique
                if oblique_index <= 0:
                    print("reset")
                    mode = "straight"
                    straight_count = 0
                    oblique_count = 0
                    continue
                print("oblique_indeX", oblique_index)
                seq[oblique_index].append(s[char_index])
                oblique_count += 1
                if oblique_count >= numRows - 2:
                    mode = "straight"
                    oblique_count = 0

            count -= 1
        print("seq", seq)

        result = []

        for i in range(numRows + 1):

            if len(seq[i]) > 0:
                result += seq[i]

        return (''.join(result))

    ''' P       H
        A     S I
        Y   I   R
        P L     I G
        A       N '''

    # A C

    # B D