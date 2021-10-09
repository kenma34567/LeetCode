"""
Runtime: Beats 56.02%
Memory: Beats 9.02%
"""


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        index_map = {}
        for i in range(len(nums)):
            if not nums[i] in index_map:
                index_map[nums[i]] = [i]
            else:
                index_map[nums[i]].append(i)

        print(index_map)

        for i in range(len(nums)):
            num = nums[i]
            # if num > target:
            # continue
            index = -1
            print("target-num", target - num)
            if target - nums[i] in index_map:
                index = index_map[target - nums[i]][0]
            print("found?", index)
            if index > -1:
                value_1 = nums[i]
                value_2 = nums[index]
                index_1 = index_map[value_1][0]
                index_2 = index_map[value_2][0]
                if index_1 == index_2:
                    if len(index_map[value_2]) > 1:
                        index_2 = index_map[value_2][1]
                    else:
                        continue
                return [index_1, index_2]

