
public class HandshakeFind {
    public static void main(String[] args) {
    int total=5;
    System.out.print(Handshake(total));
  }
  public static int Handshake(int total){
  int answer=(total*(total-1))/2;
  return answer;
}
}