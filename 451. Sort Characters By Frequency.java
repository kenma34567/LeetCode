class Solution {
    public String frequencySort(String s) {
        Map<Character, Integer> char2Freq = new HashMap<Character, Integer>();
        Map<Integer, List<Character>> freq2Char = new HashMap<Integer, List<Character>>();
        String ans = "";

        for (Character c: s.toCharArray()) char2Freq.put(c, char2Freq.getOrDefault(c, 0)+1);

        for (Map.Entry<Character, Integer> entry: char2Freq.entrySet()) {
            List<Character> chars = freq2Char.getOrDefault(entry.getValue(), new ArrayList<Character>());
            chars.add(entry.getKey());
            freq2Char.put(entry.getValue(), chars);
        }
        //System.out.println("CHECK " + freq2Char);

        for (int i=s.length(); i>=0; i--) {
            if (freq2Char.containsKey(i)) {
                for (Character c: freq2Char.get(i)) {
                    ans += String.join("", Collections.nCopies(i, String.valueOf(c)));
                }
            }
        }

        return ans;
    }
}