package programmers.level1;

public class PushKeypad {
    public static void main(String[] args) {
        String hand = "right";
        int[] numbers = {1,3,4,5,8,2,1,4,5,9,5};
        String result = "";

        int[][] keyPad = {{3,1},{0,0},{0,1},{0,2},{1,0},{1,1},{1,2},{2,0},{2,1},{2,2}}; //키패드 배열
        int[] left = {3,0}; //왼손 초기값
        int[] right = {3,2}; //오른손 초기값
        String myHand = hand.equals("left") ? "L" : "R";

        for(int num : numbers) {
            int leftDistance = (Math.abs(keyPad[num][0]-left[0])+Math.abs(keyPad[num][1]-left[1]));
            int rightDistance = (Math.abs(keyPad[num][0]-right[0])+Math.abs(keyPad[num][1]-right[1]));
            switch (num) {
                case 1: case 4: case 7:
                    result+="L";
                    left = keyPad[num];
                    break;
                case 3: case 6: case 9:
                    result+="R";
                    right = keyPad[num];
                    break;
                default:
                    if( leftDistance < rightDistance) {
                        result+="L";
                        left = keyPad[num];
                    } else if(leftDistance > rightDistance) {
                        result+="R";
                        right = keyPad[num];
                    } else {
                        result+=myHand;
                        if(myHand.equals("L")) { left = keyPad[num]; }
                        else { right = keyPad[num]; }
                    }
                    break;
            }
        }
    }
}