package programmers.level2;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.Stack;
import java.util.stream.IntStream;

public class TargetNumber {
    public static void main(String[] args) {
        int[] numbers = {1, 1, 1, 1, 1};
        int target = 3;
    //    int sum = IntStream.of(numbers).sum();

        System.out.println(" result "+recursion(numbers, target, 0, numbers.length-2, numbers.length-1));
    }

    static Integer recursion(int[] numbers, int target, int st, int ed, int cnt) {
        Stack<Integer> stackList = new Stack<>();
        int sum = 0;
        int result = 0;

        for(int i=0; i<ed; i++) {
            sum+=(numbers[i]*-1);
            stackList.add(numbers[i]*-1);
        }

        System.out.println(sum);
        /*if(target==sum) {
            result+=1;
        }
        if(st==ed-1) {
            return result+recursion(numbers, target, st-1, ed);
        }*/
      /*  if(target==sum && st!=ed) {
            return 1+recursion(numbers, target, st+1, ed);
        } else if (target!=sum) {
            return 0+recursion(numbers, target, st+1, ed);
        }*/
        return result;
    }
}
