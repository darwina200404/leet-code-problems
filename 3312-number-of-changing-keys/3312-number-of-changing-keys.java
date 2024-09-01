class Solution {
    public int countKeyChanges(String s) {
        int result=0;
        s=s.toLowerCase();
        char[]ch=s.toCharArray();
        for(int i=1;i<s.length();i++){
            if(ch[i]!=ch[i-1]){
                result++;
            }
        }
        return result;
    }
}