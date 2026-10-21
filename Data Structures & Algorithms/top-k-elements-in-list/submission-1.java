class Solution {
    public int[] topKFrequent(int[] nums, int k) {
        Map<Integer, Integer> frequencyMap = new HashMap<>();
        for (int n : nums) {
            frequencyMap.put(n, frequencyMap.getOrDefault(n, 0) + 1);
        }

        // bucket[i] = list of numbers that appear exactly i times
        List<Integer>[] bucket = new List[nums.length + 1];
        for (int key : frequencyMap.keySet()) {
            int frequency = frequencyMap.get(key);
            if (bucket[frequency] == null) {
                bucket[frequency] = new ArrayList<>();
            }
            bucket[frequency].add(key);
        }

        // Last step: go from highest frequency down, grab numbers until we have k
        int[] result = new int[k];
        int index = 0;
        for (int i = bucket.length - 1; i >= 0; i--) {
            if (bucket[i] != null) {
                for (int num : bucket[i]) {
                    result[index] = num;
                    index++;
                    if (index == k) {
                        return result;
                    }
                }
            }
        }
        return result;
    }
}