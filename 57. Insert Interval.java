class Solution {
    public int[][] insert(int[][] intervals, int[] newInterval) {
        List<int[]> updated = new ArrayList<>();
        int newStart = newInterval[0], newEnd = newInterval[1];
        boolean addedNew = false;

        for (int i=0; i<intervals.length; i++) {
            int start = intervals[i][0];
            int end = intervals[i][1];

            // add directly for interval < newInterval
            if (end < newStart) {
                updated.add(intervals[i]);
                continue;
            }

            // add directly for interval > newInterval; also add newInterval once
            if (start > newEnd) {
                if (!addedNew) updated.add(new int[]{newStart, newEnd});
                if (start > newEnd) updated.add(intervals[i]);
                addedNew = true;
                continue;
            }

            // merge interval
            if (end >= newStart) {
                newStart = Math.min(start, newStart);
            }
            newEnd = Math.max(end, newEnd);
        }

        if (!addedNew) updated.add(new int[]{newStart, newEnd});

        int[][] ans = new int[updated.size()][2];
        for (int i=0; i<updated.size(); i++) {
            ans[i][0] = updated.get(i)[0];
            ans[i][1] = updated.get(i)[1];
        }

        return ans;
    }
}