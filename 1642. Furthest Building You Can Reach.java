class Solution {
    public int furthestBuilding(int[] heights, int bricks, int ladders) {
        //int[] bricksNeeded = new int[heights.length];
        PriorityQueue<Integer> heightHeap = new PriorityQueue<Integer>(Collections.reverseOrder());
        /*for (int i=0; i<heights.length-1; i++) {
            bricksNeeded[i] = Math.max(0, heights[i+1]-heights[i]);
        }
        System.out.println("C " + Arrays.toString(bricksNeeded));*/

        for (int i=0; i<heights.length-1; i++) {
            int height = heights[i+1] - heights[i];
            if (height <= 0) continue;

            heightHeap.add(height);
            bricks -= height;
            if (bricks < 0) {
                if (ladders == 0) return i;

                int maxHeight = heightHeap.poll();
                bricks += maxHeight;
                ladders--;
            }
        }

        return heights.length-1;
    }
}