package programmers.level2;

public class StringCompression2 {
    public static void main(String[] args) {
        //못풀어서 다른사람 풀이 공부함. (아직 이해 못 함. 속도가 빠르다고 함.)
        String s = "abcabcabcabcdededededede";

        int min = s.length(); //현재 문자열의 길이
        int len = s.length()/2+1; //반복될 문자열의 최대 길이

        //반복 문자열을 1부터 돌려준다.
        for(int i = 1; i < len; i++) {
            String before = "";
            int sum = 0;
            int cnt = 1;
            //j는 0부터 시작한다
            for(int j = 0; j < s.length();) {
                int start = j; //시작 숫자는 0
                j = (j+i > s.length()) ? s.length():j+i; //문자열 길이보다 반복되는 문자열이 길다면 문자열 길이를 반환, 아니라면 j+i 를 반환한다.
                String temp = s.substring(start, j); //j를 0부터 시작한 이유, substring 에서 0이 첫 번째 자리이기 때문이다. 시작숫자부터 i를 더한 수까지 문자열을 저장한다.
                if(temp.equals(before)) { //이전에 돌고 있는 문자열(반복중인 문자열) 이라면 cnt +1 을 해준다.
                    cnt++;
                } else { //다른 문자열이라면
                    if(cnt != 1) {  //그리고 cnt 초기값인 1이 아니라면
                        sum += (int)Math.log10(cnt)+1; // ?.. 자리수를 왜 구하지
                    }
                    cnt = 1;
                    sum+=before.length(); //이전 문자열의 길이를 합산해준다.
                    before = temp; //새로운 반복 문자열을 넣어준다.
                }
            }
            sum+=before.length();
            if(cnt != 1) {
                sum += (int)Math.log10(cnt)+1;
            }
            min = (min > sum) ? sum : min;
        }
        System.out.println(min);
    }
}
