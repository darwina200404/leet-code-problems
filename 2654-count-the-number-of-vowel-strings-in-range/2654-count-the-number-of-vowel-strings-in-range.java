class Solution {
    public int vowelStrings(String[] words, int left, int right) {
        int vowelstring=0;
        for(int i=left;i<=right;i++){
            if(isvowelstring(words[i]))
                vowelstring++;
            
        }
        return vowelstring;
    }
    public static boolean isvowelstring(String str){
        char[]vowels={'a','e','i','o','u'};
        char first=str.charAt(0);
        boolean First=false;
        boolean Last=false;
        char last=str.charAt(str.length()-1);
        for(int j=0;j<vowels.length;j++){
            if(first==vowels[j])
                 First= true;
            
            if(last==vowels[j])
                Last=true;
          
        }
          
            return First && Last;
    }
}