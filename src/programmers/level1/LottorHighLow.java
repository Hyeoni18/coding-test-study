package programmers.level1;

public class LottorHighLow {
    public static void main(String[] args) {
        System.out.println("로또의 최고 순위와 최저 순위");
        int[] lottos = {44,1,0,0,31,25};
        int[] win_nums = {31,10,45,1,6,19};
        solution(lottos,win_nums);
    }

    public static int[] solution(int[] lottos, int[] win_nums) {
        int[] answer = {};
        int jackpot = 0; //맞춘 숫자
        int zeroNum = 0; //지워진 숫자

        for(int lotto : lottos) {   //1.로또 숫자를 돌린다.
            if(lotto == 0) {    //2.지워진 숫자는 카운트 해준 후 for 문을 벗어난다.
                zeroNum++;
                continue;
            }

            for(int winNum : win_nums) { //3.당첨번호를 돌려준다.
                if(lotto==winNum) { //4.숫자가 동일할 경우 카운트 해준다.
                    jackpot++;
                    break;
                }
            }
        }
        //5.jackpot=2, zeroNum=2 값이 나온다.
        answer = new int[]{getGrade(jackpot+zeroNum),getGrade(jackpot)}; //당첨순위를 조회한다.
        return answer;
    }

    public static int getGrade(int i) {
        switch (i) {
            case 6:
                return 1;
            case 5:
                return 2;
            case 4:
                return 3;
            case 3:
                return 4;
            case 2:
                return 5;
            default:
                return 6;
        }
    }
}
