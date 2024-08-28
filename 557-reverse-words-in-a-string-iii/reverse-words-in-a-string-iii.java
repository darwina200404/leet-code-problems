class Solution {
    public String reverseWords(String s) {
        String[]arr=s.split(" ");
        StringBuilder  news= new StringBuilder();

        for(String ss:arr){
            StringBuilder sb=new StringBuilder(ss);
            String str=sb.reverse().toString();
             news=news.append(str).append(" ");
        }
        
        return news.toString().trim();
    }
}