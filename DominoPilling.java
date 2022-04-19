import java.util.*;
public class DominoPilling {
    public int dom(int m, int n){
        int area = m * n;
        return area / 2;
    }
    public static void main(String[] args){
        Scanner in = new Scanner(System.in);
		DominoPilling d = new DominoPilling();
		int m = in.nextInt();
		int n = in.nextInt();
		System.out.println(d.dom(m, n));
    }
}
