import java.util.*;

public class FindFrequency {
    public static void main(String[] args) {
        int[]arr={1,2,3,4,4,4,8,9,9,2,3};
        int n=arr.length;
        HashMap<Integer,Integer>map=new HashMap<>();
        for(int i=0;i<n;i++){
            if(map.containsKey(arr[i])){
                //map.put(arr[i],map.get((arr[i])+1))
                map.put(arr[i], map.get(arr[i]) + 1);
            }
            else{
                map.put(arr[i],1);
            }
        }
        for(Map.Entry<Integer,Integer>entry:map.entrySet()){
            System.out.println(entry.getKey()+" "+entry.getValue());

        }

    }
}
