#include <iostream>
#include <vector>

using namespace std;

int main()
{
    vector<pair<int, int>> inputs;
    int tc;
    cin >> tc;

    for (int i = 0; i < tc; i++)
    {
        int temp[2];
        cin >> temp[0] >> temp[1];
        inputs.push_back(make_pair(temp[0], temp[1]));
    }

    for (int i = 0; i < tc; i++)
    {
        vector<int> range;
        for (int j = 1; j <= inputs[i].first; j++)
        {
            range.push_back(j);
        }

        bool layup = false;
        vector<int> rest;
        int ll = 2 * range.size();

        for (int j = 0; j < ll && rest.size() < inputs[i].second; j++)
        {
            int head = range.front();
            range.erase(range.begin());

            if (layup)
            {
                range.push_back(head);
                layup = false;
            }
            else
            {
                rest.push_back(head);
                layup = true;
            }
        }

        cout << rest.back() << endl;
    }
}