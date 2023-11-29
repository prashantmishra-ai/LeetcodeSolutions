public class Solution {
    // you need to treat n as an unsigned value
    public int hammingWeight(int n) {
              int count = 0;

        // Loop through all 32 bits of the integer
        for (int i = 0; i < 32; i++) {
            // Check if the ith bit is 1
            if ((n & (1 << i)) != 0) {
                count++;
            }
        }

        return count;
    }
}