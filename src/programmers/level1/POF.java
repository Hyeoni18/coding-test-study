package programmers.level1;

import java.util.Arrays;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
import java.util.stream.Collectors;
import java.util.stream.DoubleStream;

public class POF {
    public static void main(String[] args) {
        int N = 5; //스테이지 개수
        int[] stages = {2, 1, 2, 6, 2, 4, 3, 3};
        int[] answer = new int[N];

        double[] pof = new double[N];
        int user = stages.length;

        for(int i : stages) {
            if(i!=N+1) pof[i-1]+=1;
        }

        Map<Integer, Double> map = new HashMap<>();
        for(int i=0; i<pof.length; i++) {
            double temp=pof[i];
            map.put(i, pof[i]/=user);
            user-=temp;
        }

        List<Double> doubleList = DoubleStream.of(pof).sorted().boxed().collect(Collectors.toList());

        int cnt = 0;
        while(N-->0) {
            for (Integer key : map.keySet()) {
                Double value = map.get(key);
                if(doubleList.get(N).equals(value)) {
                    answer[cnt]=key+1;
                    map.put(key,null);
                    break;
                }
            }
            cnt++;
        }
    }
}
