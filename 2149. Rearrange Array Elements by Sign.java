class Solution {
    public int[] rearrangeArray(int[] nums) {
        int[] ans = new int[nums.length];
        int pos = 0;
        int neg = 1;
        int counter = 0;

        while (counter < nums.length) {
            if (nums[counter] > 0) {
                ans[pos] = nums[counter];
                pos += 2;
            } else {
                ans[neg] = nums[counter];
                neg += 2;
            }
            counter++;
        }

        return ans;
    }
}
