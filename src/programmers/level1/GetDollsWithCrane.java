package programmers.level1;

import com.sun.org.apache.bcel.internal.generic.PUSH;

import java.util.*;

public class GetDollsWithCrane {
    public static void main(String[] args) {
        int[][] board = {{0,0,0,0,0},{0,0,1,0,3},{0,0,5,0,1},{4,0,4,4,0},{3,5,1,3,1}};
        int[] moves = {1,5,3,5,1,1,4};
        int result = 0;

        Stack<Integer> gets = new Stack<>();
        Map<Integer, Object> map = new HashMap<>();
        int cnt = 0;
        for(int[] line : board) {

            if(cnt==0) {
                for(int i=0; i<line.length; i++) {
                    Queue<Integer> queue = new LinkedList<>();
                    queue.add(line[i]);
                    map.put(cnt++, queue);
                }
            } else {
                for(int i=0; i<map.size(); i++) {
                    Queue<Integer> queue = (Queue<Integer>) map.get(i);
                    queue.add((line[i]));
                    map.put(i, queue);
                }
            }

        }

        for(int i=0; i<map.size(); i++) {
            Queue<Integer> queue = (Queue<Integer>) map.get(i);
            //queue.size()!=1 은 queue 값이 전부 0 이라 검색할 값이 없을 때 나는 런타임 에러 를 방지
            while(queue.peek()==0 && queue.size()!=1) { queue.remove(); }
        }

        int after = 0;
        int before = 0;
        for(int find : moves) {
            Queue<Integer> queue = (Queue<Integer>) map.get(find-1);
            if(queue.peek()!=null) {after=queue.peek();queue.remove();} else { continue;};
            if(after != before) { gets.push(after); before=after; }
            else { gets.pop(); result+=2; };
            //gets.size()!=0 은 마지막 값을 pop 후 before 에 넣어줄 gets.peek() 값이 없을 때 나는 런타임 에러를 방지
            if(gets.size()!=0){before=gets.peek();}
        }
    }
}
