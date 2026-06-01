class Solution {
    public int lengthOfLongestSubstring(String s) {
        int max_len = 0;
        int left = 0;
        HashSet<Character> streak = new HashSet<>();

        for (int i = 0; i < s.length(); i ++) {
            while (streak.contains(s.charAt(i))) { 
                streak.remove(s.charAt(left));
                left ++;
            }

            streak.add(s.charAt(i));
            max_len = Math.max(i - left + 1 , max_len);
        }

        return max_len;
    }

}
