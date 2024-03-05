class Solution {
    public int minimumLength(String s) {
        int left = 0, right = s.length()-1;
        while (left < right && s.charAt(left) == s.charAt(right)) {
            //System.out.println("start " + left + " " + right + " " + s.charAt(left));
            while (left < right && s.charAt(left) == s.charAt(left+1))
                left++;

            while (left < right && s.charAt(right) == s.charAt(right-1))
                right--;

            left++;
            right--;
        }

        //System.out.println("final " + left + " " + right);
        return left > right? 0: right-left+1;
    }
}