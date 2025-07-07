class Solution {
    public int arithmeticTriplets(int[] nums, int diff) {
        int count=0;
        HashMap<Integer,Integer>map=new HashMap<>();
        for(int i=0;i<nums.length;i++){
            map.put(nums[i],i);
        }
        for(int num:nums){
            if(map.containsKey(num+diff)&&map.containsKey(2*diff+num)){
                count++;
            }
        }
        return count;


    }
}