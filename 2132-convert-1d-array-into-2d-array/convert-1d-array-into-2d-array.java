class Solution {
    public int[][] construct2DArray(int[] original, int m, int n) {
        int[][]newarr=new int[m][n];
        if(m*n!=original.length)
            return new int[][]{};
        
           
        for(int i=0;i<original.length;i++){
            newarr[i/n][i%n]=original[i];
        }


        return newarr;
    }
}