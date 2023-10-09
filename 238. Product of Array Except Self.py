class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        """
            [1, 2, 3, 4]
            prefix  -> [1, 2, 6, 24]    loop nums from start
            postfix -> [24, 24, 12, 4]  loop nums from back
            ans[i] = prefix[:i] * postfix[i:] --> can use 2 integers to store the product

        """

        prefixProduct = 1
        postfixProduct = 1
        ans = [0] * len(nums)

        for i in range(len(nums)):
            ans[i] = prefixProduct
            prefixProduct *= nums[i]

        for i in range(len(nums) - 1, -1, -1):
            print("back", i, postfixProduct)
            ans[i] *= postfixProduct
            postfixProduct *= nums[i]

        print("ans", ans)

        return ans
