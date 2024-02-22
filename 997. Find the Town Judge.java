class Solution {
    public int findJudge(int n, int[][] trust) {
        int judge = -1;
        Map<Integer, Integer> inMap = new HashMap<>();
        Map<Integer, Integer> outMap = new HashMap<>();

        for (int[] t: trust) {
            outMap.put(t[0], outMap.getOrDefault(t[0], 0) + 1);
            inMap.put(t[1], inMap.getOrDefault(t[1], 0) + 1);
        }

        for (int i=1; i<=n; i++) {
            if (judge != -1 && outMap.getOrDefault(i, 0) == 0) return -1;    // 2 or more people dont trust ppl
            if (outMap.getOrDefault(i, 0) == 0) judge = i;
        }

        if (judge != -1 && inMap.getOrDefault(judge, 0) == n-1) return judge;

        return -1;
    }
}