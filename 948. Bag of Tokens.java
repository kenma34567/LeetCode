class Solution {
    public int bagOfTokensScore(int[] tokens, int power) {
        Arrays.sort(tokens);
        //System.out.println("T " + Arrays.toString(tokens));

        int points = 0;
        int left = 0, right = tokens.length-1;
        while (left <= right) {
            //System.out.println("po " + power + " " + tokens[left] + " " + tokens[right]);
            if (power >= tokens[left]) {
                power -= tokens[left];
                points++;
                left++;
            } else if (points > 0 && right > left+1) {
                power += tokens[right];
                points--;
                right--;
            } else break;
        }

        return points;
    }
}