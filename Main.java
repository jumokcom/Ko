


public class Main {
    public static void main(String[] args) {
        MyStack<Integer> stack = new MyStack<>();

        stack.push(1);
        stack.push(2);
        stack.push(3);
        stack.push(4);

        System.out.println(stack); // [1, 2, 3, 4]

        System.out.println(stack.peek()); // 4

        System.out.println(stack.search(4)); // 1
        System.out.println(stack.search(3)); // 2

        stack.pop();
        stack.pop();
        stack.pop();

        System.out.println(stack); // [1]
    }
}













