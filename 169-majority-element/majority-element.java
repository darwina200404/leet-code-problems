import java.util.HashMap;
import java.util.Map;

class Solution {
    public int majorityElement(int[] nums) {
        // Create a HashMap to store the count of each element
        HashMap<Integer, Integer> countMap = new HashMap<>();
        
        // Variable to store the majority element
        int majorityElement = nums[0];
        int majorityCount = 0;

        // Iterate through the array and count occurrences
        for (int num : nums) {
            // Update the count for the current element
            countMap.put(num, countMap.getOrDefault(num, 0) + 1);
            
            // Check if the current element is now the majority element
            if (countMap.get(num) > majorityCount) {
                majorityElement = num;
                majorityCount = countMap.get(num);
            }
        }

        return majorityElement;  // Return the majority element
    }
}
