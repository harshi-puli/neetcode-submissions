class Solution {
    public boolean isAnagram(String s, String c) {
        HashMap<Character, Integer> sCharCount = new HashMap<Character, Integer>();
        HashMap<Character, Integer> cCharCount = new HashMap<Character, Integer>();
        for (int i = 0; i < Math.max(s.length(), c.length()); i++) {
            if (i<s.length()) {
                char sChar = s.charAt(i);
                if (sCharCount.containsKey(s.charAt(i))) {
                    sCharCount.put(s.charAt(i), sCharCount.get(s.charAt(i))+1);
                }
                else {
                    sCharCount.put(s.charAt(i), 1);
                }
            }

            if (i < c.length()) {
                char cChar = c.charAt(i);
                if (cCharCount.containsKey(c.charAt(i))) {
                    cCharCount.put(c.charAt(i), cCharCount.get(c.charAt(i))+1);
                }
                else {
                    cCharCount.put(c.charAt(i), 1);
                }
            }
        }

        return cCharCount.equals(sCharCount);
    }
}
