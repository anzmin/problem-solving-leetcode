class Solution {
public:
    int romanToInt(string s) {
        int n = s.length();

        unordered_map<char, int> map = {
            {'I', 1},
            {'V', 5},
            {'X', 10},
            {'L', 50},
            {'C', 100},
            {'D', 500},
            {'M', 1000}
        };

        int prev = 0;
        int res = 0;

        for (int i = n; i >= 0; i--) {
            int curr = map[s[i]];
            if (curr >= prev) {
                res += curr;
            } else {
                res -= curr;
            }
            prev = curr;
        }
        return res;
    };
};