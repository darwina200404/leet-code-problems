
import java.util.Arrays;

public class FindLargestInArray {
    public static void main(String[] args) {
        int[]arr1={2,5,1,3,0};
        Arrays.sort(arr1);
        System.out.println(arr1.length-1);
    }
}
// time complexity of O(n log n). The space complexity is O(1) 