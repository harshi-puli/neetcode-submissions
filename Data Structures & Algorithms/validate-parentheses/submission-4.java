class Solution {
    public boolean isValid(String s) {
        Stack<Character> stack = new Stack<Character>();
        Map<Character, Character> complement = new HashMap<>();
        complement.put('(',')');
        complement.put('{','}');
        complement.put('[',']');

        char[] c = s.toCharArray();

        for (int i = 0; i < s.length(); i++) {
            char current = c[i];

            if (complement.containsKey(current)) {
                stack.push(current);
            }
            else {
                if (stack.empty() || current != complement.get(stack.peek())) {          
                    return false;
                }

                stack.pop();
            }
        }
        return stack.empty(); 
    }
}
