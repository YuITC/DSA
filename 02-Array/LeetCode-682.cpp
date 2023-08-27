class Solution {
public:
    int calPoints(vector<string>& operations) {
        stack<int> record;
        for (string S : operations)
        {
            if (S == "C")
                record.pop();
            else if (S == "D")
                record.push(record.top()*2);
            else if (S == "+")
            {
                int f1 = record.top();
                record.pop();
                int f2 = record.top();
                record.push(f1);
                record.push(f1+f2);
            }
            else
                record.push(stoi(S));
        }
        int ans = 0;
        while (!record.empty())
        {
            ans += record.top();
            record.pop();
        }
        return ans;
    }
};
