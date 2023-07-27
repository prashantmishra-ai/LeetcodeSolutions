class Solution {
public:
    bool isPalindrome(int x) {
        long long int num = 0, last_digit;
        long long int org = x;
            while(x>0){
                last_digit = x%10;
                num = num*10+last_digit;
                x = x/10;
            }
        return org==num;
    }
};