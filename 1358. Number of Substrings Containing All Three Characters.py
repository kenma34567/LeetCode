class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        left = 0
        count = 0
        count_dict = defaultdict(int)

        for right, right_char in enumerate(s):
            count_dict[right_char] += 1

            while len(count_dict) == 3:
                count += len(s) - right

                left_char = s[left]
                count_dict[left_char] -= 1
                if count_dict[left_char] == 0:
                    count_dict.pop(left_char)

                left += 1

        return count
