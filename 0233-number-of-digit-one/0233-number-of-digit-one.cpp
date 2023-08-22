class Solution {
public:
int countDigitOne(int n) {
    int count = 0;
    for (long long p = 1; p <= n; p *= 10) {
        int left = n / (p * 10);
        int currentDigit = (n / p) % 10;
        int right = n % p;
        
        if (currentDigit == 0) {
            count += left * p;
        } else if (currentDigit == 1) {
            count += left * p + right + 1;
        } else {
            count += (left + 1) * p;
        }
    }
    return count;
}
};