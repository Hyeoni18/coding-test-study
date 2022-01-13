package programmers.level1;

public class PushKeypad {
    public static void main(String[] args) {
        String hand = "right";
        int[] numbers = {1,3,4,5,8,2,1,4,5,9,5};
        String result = "";

        int[][] array = {{1,2,3}, {4,5,6}, {7,8,9},{0,0,0}}; //키패드 배열
        int[] left = {3,0}; //왼손 초기값
        int[] right = {3,2}; //오른손 초기값

        for(int num : numbers) {
            int[] compare = new int[2];
            compare = findNumLocation(num);
            int one = compare[0];
            int two = compare[1];
            if(num==1 || num==4 || num==7) {
                result+="L";
                left = compare.clone();
            } else if(num==3 || num==6 || num==9) {
                result+="R";
                right = compare.clone();;
            } else {
                if((Math.abs(one-left[0])+Math.abs(two-left[1])) < (Math.abs(one-right[0])+Math.abs(two-right[1]))) {
                    result+="L";
                    left = compare.clone();
                } else if((Math.abs(one-left[0])+Math.abs(two-left[1])) > (Math.abs(one-right[0])+Math.abs(two-right[1]))) {
                    result+="R";
                    right = compare.clone();
                } else {
                    if(hand.equals("left")) { result+="L"; left = compare.clone(); }
                    else { result+="R"; right = compare.clone(); }
                }
            }
        }
    }

    static int[] findNumLocation(int num) {
        switch (num) {
            case 1:
                return new int[]{0,0};
            case 2:
                return new int[]{0,1};
            case 3:
                return new int[]{0,2};
            case 4:
                return new int[]{1,0};
            case 5:
                return new int[]{1,1};
            case 6:
                return new int[]{1,2};
            case 7:
                return new int[]{2,0};
            case 8:
                return new int[]{2,1};
            case 9:
                return new int[]{2,2};
            case 0:
                return new int[]{3,1};
            default:
                return null;
        }
    }
    //속도가 너무 느림, 코드가 너무 복잡함, 
}