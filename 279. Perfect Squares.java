class Solution {
    public int numSquares(int n) {
        if (Math.ceil(Math.sqrt(n)) == Math.floor(Math.sqrt(n))) return 1;

        Integer[] dp = new Integer[n+1];
        //Arrays.fill(dp, 0);
        dp[0] = 0;
        for (int i=1; i<=n; i++) {
            if (i*i < dp.length) dp[i*i] = 1;
            if (dp[i] == null) dp[i] = i;
        }

        for (int i=1; i<=n; i++) {
            for (int j=1; j*j<=i; j++) {
                int target = i-j*j;
                //System.out.println("running " + i + " " + j + " " + target);
                if (target < 0) continue;
                dp[i] = Math.min(dp[i], dp[target]+1);
            }
        }
        //System.out.println("C " + Arrays.toString(dp));


        return dp[n];
    }
}