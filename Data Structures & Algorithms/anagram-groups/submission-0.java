class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        HashMap<String, List<String>> map1 = new HashMap<>();
        for(int i = 0; i < strs.length; i++){
            char[] chars = strs[i].toCharArray();
            Arrays.sort(chars);
            String sorted = new String(chars);
            if(!map1.containsKey(sorted)){
                map1.put(sorted,new ArrayList<>());
            }
            map1.get(sorted).add(strs[i]);
        }
        return new ArrayList<>(map1.values());
    }
}
