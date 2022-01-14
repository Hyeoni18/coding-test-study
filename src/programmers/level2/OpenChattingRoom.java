package programmers.level2;

import java.util.HashMap;
import java.util.Map;

public class OpenChattingRoom {
    public static void main(String[] args) {
        String[] record = {"Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"};

        Map<String, Object> userMap= new HashMap<>();
        Map<Integer ,Object> massage = new HashMap<>();
        int cnt =0;
        for(String text : record) {
            switch (text.split(" ")[0]) {
                case "Enter":
                    massage.put(cnt++,text.split(" ")[1]+",님이 들어왔습니다.");
                    userMap.put(text.split(" ")[1],text.split(" ")[2]);
                    break;
                case "Leave":
                    massage.put(cnt++,text.split(" ")[1]+",님이 나갔습니다.");
                    break;
                case "Change":
                    userMap.put(text.split(" ")[1],text.split(" ")[2]);
                    break;
            }
        }
        String[] answer = new String[massage.size()];
        for(int i=0; i<massage.size(); i++) {
            String userId = userMap.get(massage.get(i).toString().split(",")[0]).toString();
            answer[i] = userId+massage.get(i).toString().split(",")[1];
        }

        System.out.println(answer[0]);
        //우오ㅏ 처리속도 엄청 느려,, 미쳤다,,
    }
}
