class Solution {
public:
        void backtrack(vector<vector<int>>& results, vector<int>& combination, int start, int n, int k) {
        // if combination is of size k, add to results and return
        if (combination.size() == k) {
            results.push_back(combination);
            return;
        }
        // iterate from the current number up to n
        for (int i = start; i <= n; i++) {
            // add current number to the combination
            combination.push_back(i);
            // recurse with next number
            backtrack(results, combination, i + 1, n, k);
            // remove last added number to try another combination
            combination.pop_back();
        }
    }
    vector<vector<int>> combine(int n, int k) {
                vector<vector<int>> results;
        vector<int> combination;
        backtrack(results, combination, 1, n, k);
        return results;
    }
};