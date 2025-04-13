
public class bruteforce {
    public int solution(int n) {
        //이진법
        String binary = Integer.toBinaryString(n);
        //System.out.println(binary);
        long limit = binary.chars().filter(c -> c == '1').count();
        //System.out.println(num);
        boolean flag = true;
        int num = n+1;
        while(flag){
            String numb = Integer.toBinaryString(num);
            if (numb.chars().filter(c -> c== '1').count() == limit){
                break;
            } else{
                num++;
            }
        }
        return num;
    }
}
