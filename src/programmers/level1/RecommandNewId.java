package programmers.level1;

import java.util.Locale;

public class RecommandNewId {
    static boolean flag = true;

    public static void main(String[] args) {
        //아이디 길이 3자 이상 15자 이하
        //알파벳 소문자, 숫자, 빼기(-), 밑줄(_), 마침표(.)만 사용 가능
        //마침표는 처음과 끝, 연속으로 사용 불가
        String id = ".abcdefghijklmn.p";

        id = id.toLowerCase(); //1단계 대문자 -> 소문자로 변경
        String match = "[^0-9a-z-_.]"; //숫자, 소문자, -, _, . 제외한 문자
        id = id.replaceAll(match, ""); //2단계 빼고 다 제거
        while (flag) {
            id = chap3(id); //3단계 ..을 .로 변경 (.... 같은 경우를 위해 while 실행)
        }
        flag = true;
        id = id.replaceAll("^[.]",""); //4단계 머리문자가 . 일 경우 제거
        if (id.isEmpty()) { //5단계 빈 값일 경우 a 로 치환
            id = "a";
        }
        if (id.length() >= 16) { //6단계 16글자 이상은 15 번째 까지만 표현
            id = id.substring(0, 15);
        }
        flag = true;
        id = id.replaceAll("[.]$",""); //꼬리문자가 . 일 경우 제거
        if (id.length() <= 2) { //7단계 2글자 이하일 경우 마지막 문자 반복 (3글자 될 때까지)
            char lastChar = id.charAt(id.length() - 1);
            id = String.format("%-3s", id).replace(' ', lastChar);
        }
    }

    static String chap3 (String id) {
        if(id.contains("..")){
            id = id.replace("..", ".");
        } else {
            flag = false;
        }
        return id;
    }
}
