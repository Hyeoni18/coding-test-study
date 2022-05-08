package programmers.level2;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.Stack;
import java.util.stream.IntStream;

public class TargetNumber {
    static int answer;

    public static void main(String[] args) {
        int[] numbers = {1, 1, 1, 1, 1};
        int target = 3;
        // 1. answer은 전역변수로 선언.
        answer = 0;

        // 2. dfs수행.
        dfs(numbers,target,0,0);
    }
    // 3. dfs(numbers, target, idx:몇 번째 인덱스인지, sum: idx까지 누적된 값).
    static void dfs(int[] numbers,int target,int idx,int sum){
        System.out.println("IDX : "+idx);
        // 4. 모든 정수를 탐색했을 때,
        if(idx == numbers.length){
            System.out.println("여긴 언제와 ? "+idx+" , sum 은 ? "+sum);
            // 5. 누적합이 target과 동일하면 answer++ 후 메소드 종료.
            if(sum == target) answer++;
            return;
        }

        // 6. 현재 인덱스의 정수를 +로 합해준다.
        sum+=numbers[idx];
        System.out.println("IDX : "+idx+" 의 sum : "+sum+" 넘버,,, : "+numbers[idx]);
        // 7. 다음 인덱스 dfs 수행.
        dfs(numbers,target,idx+1,sum);
        // 8. 6.의 값을 다시 빼준 뒤,
        sum-=numbers[idx];
        System.out.println("IDX : "+idx+" 의 뺄셈을 한 sum : "+sum+" 넘버,,, : "+numbers[idx]);
        // 9. 현재 인덱스의 정수를 -로 합해준다.
        sum+=(-1 * numbers[idx]);
        System.out.println("IDX : "+idx+" 의 9 번째 sum : "+sum+" 넘버,,, : "+numbers[idx]);
        // 10. 다시 다음 인덱스 dfs 수행.
        dfs(numbers,target,idx+1,sum);

    }

}
