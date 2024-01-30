class Solution {
    public List<List<Integer>> threeSum(int[] nums) {

        /*
            [-4, -1, -1, 0, 1, 2]
        */

        Arrays.sort(nums);
        List<List<Integer>> ans = new ArrayList<>();
        for (int i=0; i<nums.length; i++) {
            int num1 = nums[i];
            if (i > 0 && num1 == nums[i-1]) {
                continue;
            }
            int left = i+1;
            int right = nums.length-1;
            while (left < right) {
                int num2 = nums[left];
                int num3 = nums[right];
                int result = num1+num2+num3;
                if (result == 0) {
                    System.out.println("appending" +
                                        num1 + " " + num2 + " " + num3 + " " +
                                        "(" + i + " " + left + " " + right + ")");
                    ans.add(new ArrayList<>() {{
                        add(num1);
                        add(num2);
                        add(num3);
                    }});
                    left++;
                    while (nums[left] == nums[left-1] && left < right) {
                        left += 1;
                    }
                } else if (result > 0) {
                    right--;
                } else if (result < 0) {
                    left++;
                }
            }
        }

        return ans;
    }
}