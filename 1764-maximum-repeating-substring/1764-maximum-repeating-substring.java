class Solution {
    public int maxRepeating(String sequence, String word) {
        int count=0;
        while(true){
            String words=word.repeat(count+1);
            if(!sequence.contains(words)){
                return count;
            }
            count++;
        }
    }
}