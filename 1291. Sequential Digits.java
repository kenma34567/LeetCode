class Solution {

    public List<Integer> sequentialDigits(int low, int high) {
        List<Integer> ans = new ArrayList<>();
        Queue<Integer> q = new ArrayDeque<>();
        for (int i=1; i<10; i++) {
            q.add(i);
        }

        while (!q.isEmpty()) {
            int num = q.poll();
            if (num > high) break;

            if (num >= low && num <= high) {
                ans.add(num);
            }

            int ones = (num%10);
            if (ones == 9) continue;

            int newNum = num*10 + (ones+1);
            q.add(newNum);
        }

        return ans;
    }
}