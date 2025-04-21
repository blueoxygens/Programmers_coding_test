
class Solution {
    // b의 자릿수를 구함
    public int ret_digit(int num){
        if (num == 0) return 0;
        return String.valueOf(num).length();
    }

    public int solution(int a, int b) {
        if (a == 0) return b;

        int digit_b = ret_digit(b);
        int digit_a = ret_digit(a);
        int factor1 = (int)Math.pow(10, digit_b);  // 10^digit 만큼 곱해서 a를 자리수 맞춤
        int factor2 = (int)Math.pow(10, digit_a);  // 10^digit 만큼 곱해서 a를 자리수 맞춤
        return Math.max(a * factor1 + b, b*factor2 + a);
    }
}
