class Solution {

    private void bfs(char[][] grid, int i, int j, boolean[][] visited) {
        // top, bottom, left, right
        int[][] directions = {{-1, 0}, {1, 0}, {0, -1}, {0, 1}};

        int[] startPoint = {i, j};
        Queue<int[]> q = new ArrayDeque<>();
        q.add(startPoint);

        while (!q.isEmpty()) {
            //System.out.println("----");
            int[] currentPoint = q.remove();
            i = currentPoint[0];
            j = currentPoint[1];
            //System.out.println("running " + i + " " + j);
            for (int[] d: directions) {
                int movedI = i+d[0];
                int movedJ = j+d[1];
                if (movedI >= 0 && movedI < grid.length && movedJ >= 0 &&
                    movedJ < grid[movedI].length &&
                    !visited[movedI][movedJ] &&
                    grid[movedI][movedJ] == '1') {
                    int[] newPoint = {movedI, movedJ};
                    q.add(newPoint);
                    visited[movedI][movedJ] = true;
                }
            }
        }
    }

    public int numIslands(char[][] grid) {
        boolean[][] visited = new boolean[grid.length][grid[0].length];
        int ans = 0;

        for (int i=0; i<grid.length; i++) {
            for (int j=0; j<grid[i].length; j++) {
                if (grid[i][j] == '1' && !visited[i][j]) {
                    bfs(grid, i, j, visited);
                    ans += 1;
                }
            }
        }
        return ans;
    }
}