package programmers.level1;

public class PrimeNumber {
    public static void main(String[] args) {
        int[] nums = {1,2,7,6,4};
        int result = 0;

        result = recursion(nums, 0, 1, 2, nums.length-1);
        System.out.println(result);

    }
    //모든 경우의 수를 따져보기 위해 재귀 함수를 사용.
    static int recursion(int[] nums, int st, int mid, int end, int length) {
        int sum = nums[st]+nums[mid]+nums[end];
        //시작하는 수부터 남은 숫자가 3개일 경우 재귀함수 종료.
        if(st==length-2) {
            return checkPrime(sum);
        }
        //중간 숫자가 끝에서 두 번째에 다다르면 첫 번째 숫자 순서부터 +1 씩 올려준다.
        if(mid==length-1) {
            return checkPrime(sum)+recursion(nums, st+1, st+2, st+3, length);
        }
        //마지막 숫자가 끝에 다다르면 두 번째 숫자부터 +1 씩 올려준다.
        if(end==length) {
            return checkPrime(sum)+recursion(nums, st, mid+1, mid+2, length);
        }
        //3개의 숫자 중 끝에 다다른 수가 없을 경우 맨 마지막 숫자 +1 을 해준다.
        return checkPrime(sum)+recursion(nums, st, mid, end+1, length);
    }

    static int checkPrime(int pNum) {
        //소수 판별
        for(int i=2; i<pNum; i++) {
            if(pNum%i == 0) {
                return 0;
            }
        }
        return 1;
    }
}
