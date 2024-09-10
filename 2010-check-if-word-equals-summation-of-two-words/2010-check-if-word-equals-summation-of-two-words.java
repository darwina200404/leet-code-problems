class Solution {
    public boolean isSumEqual(String firstWord, String secondWord, String targetWord) {
       return numericvalue(firstWord)+numericvalue(secondWord)==numericvalue(targetWord);
    }
    public static  int numericvalue(String str){
        int sum=0;
        for(char ch:str.toCharArray()){
            sum=sum*10+(ch-'a');
    }
         return sum;
}
}