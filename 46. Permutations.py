"""
Runtime: 39 ms Beats 76.8%
Memory: 13.9 MB Beats 76.36%
backtrack
"""

class Solution:

    allPermsOfIndex = []

    def permute(self, nums: list[int]) -> list[list[int]]:

        '''
        loop all numbers from nums,
        :param nums:
        :return:
        '''

        def backtrack(visited: set[int], perm: list[int]):

            '''
            :param visited:
            :param perm:
            :return:
            '''

            #print("processing", "visited:" + str(visited))
            if len(perm) == len(nums):
                print("adding", self.allPermsOfIndex, perm)
                self.allPermsOfIndex.append(perm.copy())
                return

            print("appended", "visited:" + str(visited), "perm: " + str(perm))
            for j in range(len(nums)):
                if nums[j] in visited:
                    continue

                perm.append(nums[j])
                visited.append(nums[j])

                #print("looping", j, "visitedCopy: " + str(visited))
                backtrack(visited, perm)

                perm.pop()
                visited.pop()

        backtrack([], [])
        print("HIHI", self.allPermsOfIndex)
        return self.allPermsOfIndex


if __name__ == '__main__':
    s = Solution()
    s.permute([1, 2, 3])
    print("HI", s.allPermsOfIndex)

