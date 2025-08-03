class Solution {
    public String truncateSentence(String s, int k) {

        String[]words=s.split("\\s+");
        String newWord=new String();

        for(int i=0;i<k;i++){

            newWord+=String.valueOf(words[i])+" ";
        }
        return newWord.trim();
    }
}