class Solution {
    public int[] twoSum(int[] nums, int target) {
        HashMap<Integer, Integer> counter = new HashMap<>();
        int[] result = new int[2];

        for (int i = 0; i < nums.length; i++) {
            int difference = target - nums[i];

            if (counter.containsKey(difference)) {  
                result[0] = counter.get(difference);
                result[1] = i;
            }
            counter.put(nums[i], i);
        }
        return result;
    }
}
