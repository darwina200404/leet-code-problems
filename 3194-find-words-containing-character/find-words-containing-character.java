class Solution {
    public List<Integer> findWordsContaining(String[] words, char x) {
        ArrayList<Integer>list=new ArrayList<>();
        for (int i=0;i<words.length;i++){
            String temp=words[i];
          if(temp.contains(""+x))  {
            list.add(i);
          }
        }
        return list;
    }
}