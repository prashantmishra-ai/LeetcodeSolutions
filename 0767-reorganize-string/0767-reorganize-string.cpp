class Solution {
public:
    string reorganizeString(string s) {
        vector<int> charCounts(26, 0);
        int maxCount = 0;
        char maxChar;
        
        // Count the characters and find the character with maximum occurrences
        for (char c : s) {
            if (++charCounts[c - 'a'] > maxCount) {
                maxCount = charCounts[c - 'a'];
                maxChar = c;
            }
        }

        // If any character occurs more than (n + 1) / 2 times, return an empty string
        if (maxCount > (s.size() + 1) / 2) return "";

        // Max heap ordered by character counts
        priority_queue<pair<int, char>> pq;
        for (int i = 0; i < 26; i++) {
            if (charCounts[i] > 0) {
                pq.emplace(charCounts[i], i + 'a');
            }
        }
        
        string result;
        pair<int, char> prev = {0, ' '};

        while (!pq.empty()) {
            auto [count, char_] = pq.top(); pq.pop();

            if (prev.first > 0) {
                pq.push(prev);
            }

            result.push_back(char_);
            prev = {count - 1, char_};
        }

        return result;
    }
};
