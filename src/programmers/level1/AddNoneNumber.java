package programmers.level1;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.stream.Collectors;

public class AddNoneNumber {
    public static void main(String[] args) {
        int[] numbers = {5,8,4,0,6,7,9};
        int answer = 0;

        String text = Arrays.toString(numbers);
        int[] filter = {0,1,2,3,4,5,6,7,8,9};

        for(int i : filter) {
            if(!text.contains(Integer.toString(i))) {
                answer+=i;
            }
        }
        System.out.println(answer);

        //다른사람 풀이,,,
        int sum = 45;
        for (int i : numbers) {
            sum -= i;
        }
        System.out.println(sum);
    }
}

