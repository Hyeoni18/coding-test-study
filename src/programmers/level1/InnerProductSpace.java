package programmers.level1;

public class InnerProductSpace {
    public static void main(String[] args) {
        int[] a = {1,2,3,4};
        int[] b = {-3,-1,0,2};
        int answer = 0;
        // 내적을 구하는 공식은 주어졌음, a와 b의 내적은 a[0]*b[0] + a[1]*b[1] + ... + a[n-1]*b[n-1]
        for(int i=0; i<a.length; i++) {
            answer+=(a[i]*b[i]);
        }
        System.out.println(answer);
    }
}
