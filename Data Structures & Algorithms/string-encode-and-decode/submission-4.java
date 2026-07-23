class Solution {

    public String encode(List<String> strs) {
        String encoded = "";

    
        for (String str : strs) {
            encoded += str.length() + "#" + str;  
        }

        return encoded;
    }

    public List<String> decode(String str) { 
        List<String> decoded = new ArrayList<>();
        
        int limit = str.length();
        int i = 0; 
        int wordLen = 0; 

        while (i < limit) {
            int j = i;

            while (str.charAt(j) != '#') {
                j ++;
            }

            int len = Integer.parseInt(str.substring(i, j));

            String word = str.substring(j + 1, j + 1 + len);

            decoded.add(word);

            i = j + 1 + len;
        }

        return decoded;
    }
}
