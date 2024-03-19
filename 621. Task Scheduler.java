class Solution {
    public int leastInterval(char[] tasks, int n) {
        Map<Character, Integer> countMap = new HashMap<>();
        PriorityQueue<Integer> pq = new PriorityQueue<>(Collections.reverseOrder());
        Queue<Pair<Integer, Integer>> cooldown = new ArrayDeque<>();
        int time = 0;

        for (char t: tasks) countMap.put(t, countMap.getOrDefault(t, 0)+1);
        for (Map.Entry<Character, Integer> entry: countMap.entrySet()) pq.add(entry.getValue());
        //System.out.println("pq " + pq);

        while (pq.size() > 0 || cooldown.size() > 0) {
            time++;
            if (cooldown.size() > 0 && cooldown.peek().getValue() == time) {
                Pair<Integer, Integer> taskPair = cooldown.poll();
                pq.add(taskPair.getKey());
            }
            if (pq.size() > 0) {
                Integer taskCount = pq.poll();
                //System.out.println("doing " + taskCount + " " + time);
                if (taskCount-1 > 0) {
                    Pair<Integer, Integer> taskPair = new Pair<>(taskCount-1, time+n+1);
                    cooldown.add(taskPair);
                }
            }
        }

        return time;
    }
}