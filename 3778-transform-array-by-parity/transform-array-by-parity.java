class Solution {
    public int[] transformArray(int[] nums) {
        int evenCount=0;
        int n=nums.length;
        int[]ans=new int[n];

        for (int num:nums){
           if (num % 2 == 0) {
                evenCount++;
            } 
        }
        for(int i=evenCount;i<n;i++){
            ans[i]=1;
        }
        return ans;
        
    }
}