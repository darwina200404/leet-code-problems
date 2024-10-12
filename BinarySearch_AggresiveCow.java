import java.util.Arrays;

class BinarySearch_AggresiveCow {
    public static int solve(int n, int k, int[] stalls) {
        // Sort the stalls array to arrange stall positions in increasing order
        Arrays.sort(stalls);
        
        // Define the search space for the minimum distance
        int left = 1;  // Minimum possible distance
        int right = stalls[n - 1] - stalls[0];  // Maximum possible distance
        int result = 0;  // Variable to store the maximum minimum distance

        // Binary search for the largest minimum distance
        while (left <= right) {
            int mid = (left + right) / 2;  // Calculate the middle distance
            
            // Check if we can place all cows with at least 'mid' distance apart
            if (canPlace(stalls, k, mid)) {
                result = mid;  // Update result since it's a valid distance
                left = mid + 1;  // Try for larger distances
            } else {
                right = mid - 1;  // Try smaller distances
            }
        }
        return result;  // Return the largest minimum distance
    }

    // Helper method to check if we can place k cows with at least 'mid' distance apart
    public static boolean canPlace(int[] stalls, int k, int mid) {
        int count = 1;  // Place the first cow in the first stall
        int lastPos = stalls[0];  // Position of the last placed cow

        // Try to place remaining cows
        for (int i = 1; i < stalls.length; i++) {
            if ((stalls[i] - lastPos) >= mid) {
                count++;  // Place another cow
                lastPos = stalls[i];  // Update last cow's position
            }
            if (count == k) {
                return true;  // All cows placed successfully
            }
        }
        return false;  // Couldn't place all cows
    }
    
    // Main method for testing
    public static void main(String[] args) {
        // Example input
        int n = 5;
        int k = 3;
        int[] stalls = {1, 2, 8, 4, 9};

        // Call the solve method
        int result = solve(n, k, stalls);
        System.out.println(result);  // Expected output: 3
    }
}
