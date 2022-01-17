package programmers.level1;

import java.util.Arrays;
import java.util.List;
import java.util.stream.Collectors;

public class UnfinishedRunner {
    public static void main(String[] args) {
        String[] participant = {"mislav", "stanko", "mislav", "ana"};
        String[] completion = {"stanko", "ana", "mislav"};

        Arrays.sort(participant);
        Arrays.sort(completion);
        int i; //i를 바깥에 선언한 이유는 배열의 맨 마지막일 경우 for문을 그냥 빠져나오게 됨.
        for ( i=0; i<completion.length; i++){

            if (!participant[i].equals(completion[i])){
                System.out.println(participant[i]);
            }
        }
        //마지막 선수를 확인하기 위해
        System.out.println(participant[i]);
    }
}
