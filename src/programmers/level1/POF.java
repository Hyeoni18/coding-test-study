package programmers.level1;

import java.util.HashMap;
import java.util.List;
import java.util.Map;
import java.util.stream.Collectors;
import java.util.stream.DoubleStream;

public class POF {
    public static void main(String[] args) {
        int N = 5; //스테이지 개수
        int[] stages = {2, 1, 2, 4, 2, 4, 3, 3};
        int[] answer = new int[N];

        double[] pof = new double[N];
        int user = stages.length;

        //각 스테이지에 유저가 얼마나 분포되어 있는지 체크
        for(int i : stages) {
            if(i!=N+1) pof[i-1]+=1;
        }

        //스테이지별로 실패율을 계산하여 map에 저장
        Map<Integer, Double> map = new HashMap<>();
        for(int i=0; i<pof.length; i++) {
            double temp=pof[i];
            if (pof[i]==0) {
                map.put(i, 0.0);
            } else {
                map.put(i, pof[i]/=user);
            }
            user-=temp;
        }
        //실패율을 오름차순으로 정렬
        List<Double> doubleList = DoubleStream.of(pof).sorted().boxed().collect(Collectors.toList());

        //오름차순이기에 N--으로 진행, 해당 실패율 값을 가지고 있는 스테이지 값을 찾는 과정.
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
    //풀긴 했지만,, 처참한 심정이다. 시간 초과 안 난 게 신기할 정도.
}
