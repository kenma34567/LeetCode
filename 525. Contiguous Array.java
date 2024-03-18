class Solution {
    public int findMaxLength(int[] nums) {
        int maxLength = 0, zero = 0, one = 0;
        Map<Integer, Integer> diff2Index = new HashMap<>();

        for (int i=0; i<nums.length; i++) {
            if (nums[i] == 0) zero++;
            if (nums[i] == 1) one++;

            int diff = one - zero;
            if (!diff2Index.containsKey(diff)) {
                diff2Index.put(diff, i);
            }

            if (one == zero) {
                maxLength = one + zero;
            } else {
                maxLength = Math.max(maxLength, i-diff2Index.get(diff));
            }

        }
        //System.out.println("C " + diff2Index);

        return maxLength;
    }
}