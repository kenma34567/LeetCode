class Solution {
    public int maxSubarrayLength(int[] nums, int k) {
        int maxLength = 0;
        int left = 0;
        Map<Integer, Integer> numCount = new HashMap<>();
        for (int right=0; right<nums.length; right++) {
            int n = nums[right];
            numCount.put(n, numCount.getOrDefault(n, 0) + 1);
            while (left <= right && numCount.get(n) > k) {
                numCount.put(nums[left], numCount.get(nums[left]) - 1);
                left++;
            }
            maxLength = Math.max(maxLength, right-left+1);
        }

        return maxLength;
    }
}