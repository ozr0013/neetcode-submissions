class Solution {
    final char DELIMETER = '#';
    public String encode(List<String> strs) {
        StringBuilder sb = new StringBuilder();
        for(String str : strs){
            sb.append(str.length());
            sb.append(DELIMETER);
            sb.append(str);
        }
        return sb.toString();
    }

    public List<String> decode(String str) {
        List<String> res = new LinkedList<>();
        char[] arr = str.toCharArray();
        for(int i = 0; i < arr.length; i++){
            // Fint the number of characters
            StringBuilder sb = new StringBuilder();
            while(arr[i] != DELIMETER){
                sb.append(arr[i]);
                i++;
            }
            i++;
            int numOfChar = Integer.valueOf(sb.toString());
            int end = i + numOfChar;
            sb = new StringBuilder();
            while(i < end){
                sb.append(arr[i]);
                i++;
            }
            i--;
            res.add(sb.toString());
        }
        return res;
    }
}
