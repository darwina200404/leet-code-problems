class Solution {
    public int removeDuplicates(int[] nums) {
        // Edge case
        if (nums.length == 0) {
            return 0;
        }
        
        // Initialize a pointer to track the unique elements
        int k = 1;
        
        // Iterate through the array starting from the second element
        for (int i = 1; i < nums.length; i++) {
            // If current element is different from previous element
            if (nums[i] != nums[i - 1]) {
                nums[k] = nums[i]; // Update nums[k] with the unique element
                k++; // Move to the next position for the next unique element
            }
        }
        
        // k now represents the number of unique elements
        return k;
    }
}
