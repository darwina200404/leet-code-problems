
public class PageFlip {

    public static void main(String[] args) {
    int total=11;
    int target=3;
  int totalFlip=total/2;
  int left=target/2;
  int right=total-left;
  System.out.print(Math.min(left,right)) ;
  }
}