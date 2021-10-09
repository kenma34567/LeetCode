"""
Runtime: Beats 69.42%
Memory: Beats 61.92%
"""


class Solution:
    num_2_letters = {
        "2": ['a', 'b', 'c'],
        "3": ['d', 'e', 'f'],
        "4": ['g', 'h', 'i'],
        "5": ['j', 'k', 'l'],
        "6": ['m', 'n', 'o'],
        "7": ['p', 'q', 'r', 's'],
        "8": ['t', 'u', 'v'],
        "9": ['w', 'x', 'y', 'z']
    }

    def to_letter(self, num: int, num_pos: int, index: int, digits: str, result: str, ans: []):

        letters = self.num_2_letters[num]
        if index == len(letters):
            print("returning!11", result)
            if len(result) == len(digits):
                ans.append(result)
                return ans
            return None

        result += letters[index]

        if num_pos == len(digits) - 1:
            print("returning!", result)
            ans.append(result)
            return ans
        else:
            # or just loop 4
            next_letters = self.num_2_letters[digits[num_pos + 1]]
            for j in range(len(next_letters)):
                self.to_letter(digits[num_pos + 1], num_pos + 1, j, digits, result, ans)

        return ans

    def letterCombinations(self, digits: str) -> List[str]:

        if len(digits) == 0:
            return

        coms = []
        first_letters = self.num_2_letters[digits[0]]

        for i in range(len(first_letters)):
            coms += self.to_letter(digits[0], 0, i, digits, "", [])

        print("COM", coms)
        return coms


