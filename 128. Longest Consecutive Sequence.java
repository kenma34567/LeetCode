class Solution {
    public int longestConsecutive(int[] nums) {
        if (nums == null || nums.length == 0) return 0;

        Set<Integer> s = new HashSet<>();
        int maxLength = 1;

        for (int i=0; i<nums.length; i++) {
            s.add(nums[i]);
        }
        //System.out.println("C " + s);

        for (int i=0; i<nums.length; i++) {
            int current = nums[i];
            if (s.contains(current-1)) continue;     // will be processed after / processed before
            int currentLength = 1;
            while (s.contains(current+1)) {
                currentLength += 1;
                current++;
            }
            maxLength = Math.max(maxLength, currentLength);
        }

        return maxLength;
    }
}
