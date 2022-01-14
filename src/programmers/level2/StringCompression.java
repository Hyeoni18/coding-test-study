package programmers.level2;

public class StringCompression {
    public static void main(String[] args) {
        //못풀어서 다른사람 풀이 공부함. (재귀 사용)
        String s = "aabbaccc";
        int answer = 0;

        //앞에서부터 해야하니까 /2 +1 까지 범위를 줬나부다
        for(int i=1; i<=(s.length()/2)+1; i++){
            int result = getSplitedLength(s, i, 1).length();
            answer = i==1 ? result : (answer>result?result:answer);
        }

        System.out.println(answer);
    }

    public static String getSplitedLength(String s, int n, int repeat){ //s 는 문자열, n 은 반복할 문자 개수, repeat 은 반복횟수인가 1 회
        if(s.length() < n) return s; //문자열보다 반복할 문자 개수가 많을 수 없으니 바로 return
        String result = "";
        String preString = s.substring(0, n); //처음부터 반복할 문자열까지 preString
        String postString = s.substring(n, s.length()); //남은 문자열 postString

        // 불일치 -> 현재까지 [반복횟수 + 반복문자] 조합
        if(!postString.startsWith(preString)){ //남은 문자열에 반복할 문자열이 없다면
            if(repeat ==1) return result += preString + getSplitedLength(postString, n, 1); //repeat 이 1이니까 preString(반복중인 문자열)을 붙여주고 다시 getSplitedLength 메소드 호출
            return result += Integer.toString(repeat) + preString + getSplitedLength(postString, n, 1); //만약 2회이상 반복된 문자열이라면, Integer.toString(repeat) 횟수를 적어주고 반복한 문자열을 적고 getSplitedLength 메소드 호출
        }
        //반복중인 문자열이 존재한다면
        return result += getSplitedLength(postString, n, repeat+1); //getSplitedLength를 호출하지만 repeat+1 에 +1 을 해줌으로써 현재 문자열이 한 번 더 돌고 있다는 것을 표시
    }
}
