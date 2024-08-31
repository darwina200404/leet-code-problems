class Solution {
    public String decodeMessage(String key, String message) {
      String keys= key.replaceAll("\\s+","");
        HashMap<Character,Character>alphabetmap=new HashMap<>();
          char value='a';
        for(int i=0;i<keys.length();i++){
            char Key=keys.charAt(i);
            if(!alphabetmap.containsKey(Key)){
            alphabetmap.put(Key,value);
            value++;
            if(value>'z')break;
            }
        }
        StringBuilder result=new StringBuilder();
        for(char c:message.toCharArray()){
            if(alphabetmap.containsKey(c)){
                result.append(alphabetmap.get(c));
            }
            else{
                result.append(c);
            }
        }
        return result.toString();
    }
}