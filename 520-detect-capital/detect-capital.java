class Solution {
    public boolean detectCapitalUse(String word) {
        if (word.equals(word.toLowerCase())){
            return true;
        }
        if (Character.isUpperCase(word.charAt(0)) && word.substring(1).equals(word.substring(1).toLowerCase())) {
            return true;
        }
        for(char ch:word.toCharArray()){
             if(Character.isLowerCase(ch)){
               
                return false;
            }

        }

          return true;
           
    }
}