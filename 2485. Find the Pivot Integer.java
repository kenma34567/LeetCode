class Solution {
    public int pivotInteger(int n) {
        int total = n * (1+n)/2;
        //System.out.println("total " + total);
        int left = 0, pivot = 1, right = total;
        while (left < right) {
            left += pivot;
            if (left == right) return pivot;
            //System.out.println("processing " + left + " " + right);
            right -= pivot;
            pivot++;
        }

        return -1;
    }
}