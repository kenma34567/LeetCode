class Solution {
    public int minimumTotal(List<List<Integer>> triangle) {
        return dfs(triangle, 0, 0, new HashMap<Pair<Integer, Integer>, Integer>());
    }

    private int dfs(List<List<Integer>> triangle, int row, int index, Map<Pair<Integer, Integer>, Integer> cache) {
        if (row >= triangle.size()) return 0;

        Pair<Integer, Integer> pair = new Pair<>(row, index);
        if (cache.containsKey(pair)) return cache.get(pair);

        int sum = triangle.get(row).get(index) +
                    Math.min(
                        dfs(triangle, row+1, index, cache),
                        dfs(triangle, row+1, index+1, cache)
                    );

        cache.put(pair, sum);
        return sum;
    }
}
