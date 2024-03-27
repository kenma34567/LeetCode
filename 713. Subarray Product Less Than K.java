class Solution {

    private int count = 0;
    public int numSubarrayProductLessThanK(int[] nums, int k) {
        int left = 0, product = 1;

        for (int right=0; right<nums.length; right++) {
            product *= nums[right];
            while (left <= right && product >= k) {
                product /= nums[left];
                left++;
            }

            //System.out.println("product " + product + " " + right + " " + left);
            count += right-left+1;

        }

        return count;
    }
}