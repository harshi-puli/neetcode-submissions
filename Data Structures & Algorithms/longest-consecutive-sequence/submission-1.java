class Solution {
    public int longestConsecutive(int[] nums) {
        int maxLen = 0;

        HashSet<Integer> record = new HashSet<>();
        for (int n: nums) {
            record.add(n);
        }

        for (int i = 0; i < nums.length; i ++) {
            int curr = nums[i];
            int len = 1;
    
            while (record.contains(curr + 1)) {
                curr += 1;
                len += 1;
            }

            if (len > maxLen) {
                maxLen = len;
            }
        }

        return maxLen;
    }
}
