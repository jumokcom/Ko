public class BracketChecker {
    public static boolean isValid(String expression) {
        MyStack<Character> stack = new MyStack<>();

        for (char ch : expression.toCharArray()) {
            if (ch == '(' || ch == '{' || ch == '[') {
                stack.push(ch);
            } else if (ch == ')' || ch == '}' || ch == ']') {
                if (stack.isEmpty()) {
                    return false; // 닫는 괄호가 여는 괄호보다 많은 경우
                }
                char top = stack.pop();
                if (!isMatchingPair(top, ch)) {
                    return false; // 괄호가 짝이 맞지 않는 경우
                }
            }
        }

        return stack.isEmpty(); // 모든 괄호가 짝이 맞아 스택이 비어있는 경우
    }

    // 괄호가 짝이 맞는지 확인하는 메소드
    private static boolean isMatchingPair(char open, char close) {
        return (open == '(' && close == ')') ||
                (open == '{' && close == '}') ||
                (open == '[' && close == ']');
    }

    public static void main(String[] args) {
        String expression1 = "{[()]}";
        String expression2 = "{[(])}";
        String expression3 = "{[()]}{";

        System.out.println(expression1 + " is valid: " + isValid(expression1));
        System.out.println(expression2 + " is valid: " + isValid(expression2));
        System.out.println(expression3 + " is valid: " + isValid(expression3));
    }
}

