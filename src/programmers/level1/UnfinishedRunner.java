package programmers.level1;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.stream.Collectors;

public class UnfinishedRunner {
    public static void main(String[] args) {
        String[] participant = {"mislav", "stanko", "mislav", "ana"};
        String[] completion = {"stanko", "ana", "mislav"};

        for(int i=0; i<participant.length; i++) {
            boolean flag = true;
            for(int j=0; j<completion.length; j++) {
                if(participant[i].equals(completion[j])) {
                    participant[i]="0";
                    completion[j]="0";
                    flag=false;
                    break;
                }
            }
            if(flag) {
                System.out.println(participant[i]);
            }
        }
    }
}
