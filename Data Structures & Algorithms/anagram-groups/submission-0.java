class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        if (strs == null | strs.length == 0) { return new ArrayList<>(); }

        Map<String, ArrayList<String>> result = new HashMap<>();

        for (String str: strs) {
            char[] c = str.toCharArray();

            Arrays.sort(c);
            String s = String.valueOf(c);

            if (!result.containsKey(s)) {
                result.put(s, new ArrayList<>());
            }
            result.get(s).add(str);
        }

        List<List<String>> finalResult = new ArrayList<>(result.values());
        return finalResult;
    }
}
