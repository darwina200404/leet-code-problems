class Solution {
    public int minTimeToType(String word) {
         int n=word.length();
        int sum=0;
        int start=(int)'a';
        for(int i=0;i<n;i++){
            int curr=(int)word.charAt(i);
            int x=Math.min(Math.abs(start-curr),26-Math.abs(start-curr));
            sum=sum+x;
            start=curr;
        }
        return sum+n;
    }
}