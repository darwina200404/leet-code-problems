
import java.util.Arrays;

public class ReverseGivenArray {
    public static void main(String[] args) {
        int[]arr1={5,4,3,2,1};
        int[]arr2=new int[arr1.length];
        int n=arr1.length;
        for(int i=n-1;i>0;i--){
            arr2[n-i]=arr1[i];
        }
        
            System.out.println(Arrays.toString(arr2));
    

    }
}
/*import java.util.Arrays;

public class ReverseGivenArray {
    public static void main(String[] args) {
        int[] arr1 = {5, 4, 3, 2, 1};  // Example array
        int n = arr1.length;

        // Reverse the array in-place
        for (int i = 0; i < n / 2; i++) {
            int temp = arr1[i];  // Swap arr1[i] with arr1[n-i-1]
            arr1[i] = arr1[n - i - 1];
            arr1[n - i - 1] = temp;
        }

        // Print the reversed array
        System.out.println(Arrays.toString(arr1));
    }
}
*/
