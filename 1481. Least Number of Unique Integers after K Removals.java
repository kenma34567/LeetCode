class Solution {
    public int findLeastNumOfUniqueInts(int[] arr, int k) {
        Map<Integer, Integer> int2CountMap = new HashMap<>();
        int[] countArr = new int[arr.length+1];
        //Map<Integer, Integer> intCount2CountMap = new HashMap<>();
        for (int n: arr) {
            int2CountMap.putIfAbsent(n, 0);
            int2CountMap.put(n, int2CountMap.get(n)+1);
        }
        //System.out.println("uieui " + int2CountMap);

        for (Integer v: int2CountMap.values()) countArr[v] += 1;
        //System.out.println("arr " + Arrays.toString(countArr));

        int result = int2CountMap.keySet().size();
        for (int i=1; i<countArr.length; i++) {
            int remove = countArr[i];
            if (k >= remove*i) {
                k -= remove*i;
                result -= remove;
            } else {
                remove = (int) Math.floor(k / i);
                result -= remove;
                break;
            }
        }
        return result;
    }
}