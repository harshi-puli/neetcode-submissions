class Solution {
    public boolean hasDuplicate(int[] nums) {
        HashSet<Integer> unique = new HashSet<Integer>();
        for (int n: nums) {
            unique.add(n);
        }

        if (unique.size() != nums.length) {
            return true;
        }
        return false;
    }
}