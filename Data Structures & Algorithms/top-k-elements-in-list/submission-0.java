class Solution {
    public int[] topKFrequent(int[] nums, int k) {
        HashMap<Integer, Integer> count = new HashMap<>();
        ArrayList<ArrayList<Integer>> freq = new ArrayList<>();

        int[] result = new int[k];
        int tracker = 0;
        for (int n: nums) {
            count.put(n, 1 + count.getOrDefault(n, 0));
        }

        for (int i = 0; i <= nums.length; i++) {
            freq.add(new ArrayList<>());
        }

        for (Map.Entry<Integer, Integer> entry: count.entrySet()) {
            freq.get(entry.getValue()).add(entry.getKey());
        }

        for (int i = nums.length; i > 0; i--) {
            if (freq.get(i).size() > 0) {
                for (int element: freq.get(i)) {
                    result[tracker] = element;
                    tracker ++;
                    if (tracker == k) {
                        return result;
                    }
                }
            }
        }  

        System.out.println(count);
        System.out.println(freq);

        return result;
    }
}
