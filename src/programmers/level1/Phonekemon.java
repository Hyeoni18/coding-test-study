package programmers.level1;

import java.util.*;
import java.util.stream.Collectors;

public class Phonekemon {
    public static void main(String[] args) {
        int[] nums = {3,3,3,2,2,4};

        ArrayList<Integer> integerArray = (ArrayList<Integer>) Arrays.stream(nums).boxed().distinct().collect(Collectors.toList());
        int answer = nums.length/2>integerArray.size() ? integerArray.size() : nums.length/2;

        //다른 사람 풀이.
        Arrays.stream(nums)
                .boxed()
                .collect(Collectors.collectingAndThen(Collectors.toSet(),
                        phonekemons -> Integer.min(phonekemons.size(), nums.length / 2)));
    }
}
