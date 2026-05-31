class Solution {
    public boolean isPalindrome(String s) {
        s = s.replaceAll("[^a-zA-Z0-9]", "").toLowerCase();
        char[] c = s.toCharArray();
        System.out.println(c);

        for (int i = 0; i < s.length(); i++) {
            int j = s.length() - 1 - i;

            if (!(c[i] == c[j])) {
                return false;
            }
        }

        return true;
    }
}
