class Solution {
    public int[] twoSum(int[] nums, int target) {
        int n = nums.length;

        // Pre-size HashMap to reduce rehashing
        java.util.HashMap<Integer, Integer> map = new java.util.HashMap<>(n);

        for (int i = 0; i < n; i++) {
            int num = nums[i];
            int complement = target - num;

            Integer index = map.get(complement);
            if (index != null) {
                return new int[]{index, i};
            }

            map.put(num, i);
        }

        return null; // faster than new int[]{} in practice
    }
}
