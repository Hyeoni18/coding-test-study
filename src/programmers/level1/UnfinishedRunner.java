package programmers.level1;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.stream.Collectors;

public class UnfinishedRunner {
    public static void main(String[] args) {
        String[] participant = {"leo", "kiki", "eden"};
        String[] completion = {"eden"};

        List<String> pList = Arrays.asList(participant);
        for(String runner : completion) {
            pList = pList.stream().filter( d -> !d.equals(runner)).collect(Collectors.toList());
        }
        System.out.println(pList.toString().getClass());

    }
}
