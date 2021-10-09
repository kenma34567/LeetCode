"""
Runtime: Beats 96.55%
Memory: Beats 96.52%
"""


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:

        ans = []

        def recur(temp_str, open_par_count, close_par_count):

            if open_par_count == n == close_par_count:
                ans.append(temp_str)

            elif close_par_count > open_par_count:  # close should never > open
                return

            elif open_par_count > n or close_par_count > n:
                return

            recur(temp_str + '(', open_par_count + 1, close_par_count)  # try to add '('
            recur(temp_str + ')', open_par_count, close_par_count + 1)  # try to add ')'

        recur("", 0, 0)

        return ans




