import java.util.*;
class Solution
{
    public int solution(String s)
    {
        int answer = -1;
        char[] arr = {};
        arr = s.toCharArray();
        ArrayDeque<String> list = new ArrayDeque<>();
        for(int i =0; i<arr.length; i++){
            list.add(String.valueOf(arr[i]));
        }
        //System.out.println(arr);
        ArrayDeque<String>stck = new ArrayDeque<>();
        while (!list.isEmpty()){
            if(stck.isEmpty()){
                stck.addLast(list.pollFirst());
            }else if(stck.peekLast().equals(list.peekFirst())){
                stck.removeLast();
                list.removeFirst();
            }else{
                stck.addLast(list.pollFirst());
            }
            //System.out.println(stck);
            //System.out.println(list);
        }
        if(stck.isEmpty()){
            answer = 1;
        }else{
            answer = 0;
        }
        return answer;
    }
}