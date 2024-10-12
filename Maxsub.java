public class Maxsub {
    public static void main(String []args){
        int[]arr=new int[]{1,2,3,4,5};
        int sum=0;
        int max=0;
        for(int i=0;i<arr.length;i++){
            for(int j=i+1;j<arr.length;j++){
                sum=arr[i]+arr[j];
                max=Integer.max(sum,max);
            }

        }
        System.out.print(max);
    }
   
}
