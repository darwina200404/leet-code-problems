public class FindNearestCombination {
    static int min = Integer.MAX_VALUE;
    static int count = 0;

    // Function to find the nearest number greater than B
    public int FindNearestGreatest(String str1, int i, int n, int B) {
        if (i == n) {
            int num = Integer.parseInt(str1);
            if (num > B && num < min) {
                min = num;
                count = 1;
            }
        } else {
            for (int j = i; j <= n; j++) {
                str1 = swap(str1, i, j); // Swap digits
                FindNearestGreatest(str1, i + 1, n, B); // Recurse to generate other permutations
                str1 = swap(str1, i, j); // Backtrack to restore the original state
            }
        }
        return min;
    }

    // Function to swap characters in a string
    public String swap(String str1, int i, int j) {
        char[] charArray = str1.toCharArray();
        char temp = charArray[i];
        charArray[i] = charArray[j];
        charArray[j] = temp;
        return String.valueOf(charArray);
    }

    public static void main(String[] args) {
        int a = 459;
        int b = 500; // Target value

        FindNearestCombination ngn = new FindNearestCombination();
        String A = Integer.toString(a); // Convert integer to string
        int length = A.length();

        // Find nearest greater number by permuting digits
        int result = ngn.FindNearestGreatest(A, 0, length - 1, b);

        // Output the result
        if (count == 1) {
            System.out.println("The nearest number greater than " + b + " is: " + result);
        } else {
            System.out.println("-1 (No valid number greater than " + b + " found)");
        }
    }
}
//The time complexity of this algorithm is O(n!) because it generates all possible permutations of the input string. 
//The space complexity is O(n) because of the recursive calls on the call stack.