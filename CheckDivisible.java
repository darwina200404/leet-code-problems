class CheckDivisible{
    public static void main(String[] args) {
        int number=24;
        int temp=number ;
        int count=0;
        while(number>0){
            int num=number%10;
            if (num!=0){
                if(temp%num==0){
                    count++;
                }
            }
            number=number/10;
        
        }
        String str=Integer.toString(temp);
        if(count==str.length())
            System.err.println("Yes");
        else  
            System.err.println("No");
    }
}
