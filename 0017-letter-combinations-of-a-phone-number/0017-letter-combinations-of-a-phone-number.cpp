class Solution {
public:
    vector<string> letterCombinations(string digits) {
        vector<string> res;
        if (digits.empty()) return res;
        vector<string> phone = {"", "", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"};
        res.push_back("");
        for (int i = 0; i < digits.size(); ++i) {
            vector<string> temp;
            string str = phone[digits[i] - '0'];
            for (int j = 0; j < str.size(); ++j) {
                for (string s : res) {
                    temp.push_back(s + str[j]);
                }
            }
            res.swap(temp);
        }
        return res;
    }
};