package programmers.level1;

import com.sun.org.apache.bcel.internal.generic.PUSH;

import java.util.*;

public class GetDollsWithCrane {
    public static void main(String[] args) {
        int[][] board = {{0,0,0,0,0},{0,0,1,0,3},{0,2,5,0,1},{4,2,4,4,2},{3,5,1,3,1}};
        int[] moves = {1,5,3,5,1,2,1,4};
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
            while(queue.peek()==0) { queue.remove(); }
        }

        int after = 0;
        int before = 0;
        for(int find : moves) {
            Queue<Integer> queue = (Queue<Integer>) map.get(find-1);
            if(queue.peek()!=null) {after=queue.peek();queue.remove();} else { continue;};
            if(after != before) { gets.push(after); before=after; }
            else if(gets.size()!=0){ gets.pop(); before=gets.peek(); result+=2; };
        }
        System.out.println(gets);
    }
}
