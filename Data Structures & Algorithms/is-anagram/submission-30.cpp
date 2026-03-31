class Solution {
public:
    bool isAnagram(string s, string t) {
        if (s.length() != t.length()) {
            return false;
        }

        unordered_map<char, int> s_c;
        unordered_map<char, int> t_c;

        for (int i = 0; i < s.length(); i++) {
            s_c[s[i]]++;
            t_c[t[i]]++;
        }

        return s_c == t_c;
    }
};
