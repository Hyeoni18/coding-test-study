package programmers.level1;

public class NumStringAndEngWord {
    public static void main(String[] args) {
        String word = "one4seveneight";
        //영단어로 된 숫자는 숫자형식으로 변경
        word=word.replaceAll("zero","0");
        word=word.replaceAll("one","1");
        word=word.replaceAll("two","2");
        word=word.replaceAll("three","3");
        word=word.replaceAll("four","4");
        word=word.replaceAll("five","5");
        word=word.replaceAll("six","6");
        word=word.replaceAll("seven","7");
        word=word.replaceAll("eight","8");
        word=word.replaceAll("nine","9");

        System.out.println(word);
        //아니 왜 4ㅈ점밖에 안 줘ㅠㅜ ㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋ
    }


}
