class Solution {

    Map<Integer, Integer> cache = new HashMap<Integer, Integer>();

    private int dfs(int[] arr, int i, int k) {
        if (i>=arr.length) return 0;
        if (cache.containsKey(i)) return cache.get(i);

        int res = 0;
        int currentMax = 0;
        for (int j=i; j<Math.min(arr.length, i+k); j++) {
            currentMax = Math.max(currentMax, arr[j]);
            int size = j-i+1;
            res = Math.max(res, dfs(arr, j+1, k) + currentMax*size);
        }

        cache.put(i, res);
        return res;
    }

    public int maxSumAfterPartitioning(int[] arr, int k) {
        return dfs(arr, 0, k);
    }
}