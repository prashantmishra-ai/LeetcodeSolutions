class Solution {
public:
    string convertToTitle(int columnNumber) {
            std::string result = "";
    
    while (columnNumber) {
        columnNumber -= 1;
        char ch = (columnNumber % 26) + 'A';
        result += ch;
        columnNumber /= 26;
    }
    
    std::reverse(result.begin(), result.end());
    return result;
    }
};