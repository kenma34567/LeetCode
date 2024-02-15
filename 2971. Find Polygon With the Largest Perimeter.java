class Solution {
    public long largestPerimeter(int[] nums) {
        //int currentPerimeter = 0;
        Arrays.sort(nums);
        long total = 0, res = -1;
        for (int n: nums) {
            if (total > n) {
                res = total + n;
            }
            total += n;
        }
        return res;

        /*long[] prefixSum = new long[nums.length];
        prefixSum[0] = nums[0];
        for (int i=1; i<nums.length; i++) {
            prefixSum[i] = prefixSum[i-1] + nums[i];
        }
        //System.out.println("sorted " + Arrays.toString(nums));
        //System.out.println("CHECK " + Arrays.toString(prefixSum));
        for (int i=nums.length-1; i>0; i--) {
            if (prefixSum[i-1] > nums[i]) {
                return prefixSum[i];
            }
        }

        return -1;*/
    }
}