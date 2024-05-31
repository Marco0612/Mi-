#include <bits/stdc++.h>
#define FOR(i,x) for(int i = 0; i < x; i++)
#define all(v) v.begin(), v.end()
#define allr(v) v.rbegin(), v.rend()

using namespace std;
typedef vector <int> vi;
typedef long long ll;
typedef string st;



int main()
{	
    int t; cin >> t;

    while(t--)
    {
        int n; 
        cin >> n;  
        map<int, int> nums;
        FOR(i, n)
        {
            int temp; cin >> temp;
            nums[temp]++;
        }

        while(!nums.empty())
        {
            vector<int> to_erase;
            for (auto& pair : nums) 
            {
                if(pair.second == 1)
                {
                    to_erase.push_back(pair.first);
                    cout <<  pair.first << " ";
                }else{
                    cout <<  pair.first << " ";
                    pair.second--;
                } 
            }
            for (int elem : to_erase)
            {
                nums.erase(elem);
            }

        }
        cout << "\n";
    }  

    return 0;
}
