class Solution {
    public int[] productExceptSelf(int[] nums) {
        int product = 1;
        int[] output = new int[nums.length];

        for (int n: nums) {
            product = product * n;
        }

        for (int i = 0; i < nums.length; i ++) {
            if (nums[i] != 0) {
                output[i] = product / nums[i];
            } 
            else {
                int p = 1;

                for (int j = 0; j < nums.length; j ++) {
                    if (j != i) {
                        p = p * nums[j];
                    }
                }

                output[i] = p;
            }
        }

        return output;
    }
}  
