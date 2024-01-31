class Solution {
    public int findMin(int[] nums) {

        int left = 0;
        int right = nums.length-1;
        int result = nums[0];

        while (left <= right) {
            int mid = left + (right-left)/2;
            result = Math.min(result, nums[mid]);
            if ((nums[left] < nums[right] && nums[left] < nums[mid])
                || (nums[left] > nums[mid] && nums[left] > nums[right])) {
                right = mid - 1;
            } else {
                left = mid + 1;
            }

        }

        return result;
    }
}