class Solution {
    public int tribonacci(int n) {
        int[]F=new int[n+5];
             if(n==0)
                return 0;
            if(n==1||n==2)
                return 1;
   F[0]=0;
        F[1]=1;
        F[2]=1;

        for(int i=0;i<n;i++){
            F[i+3]=F[i]+F[i+1]+F[i+2];
    }
             return F[n];
        
       
    }
}