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
	int t; //cin >> t;
    t = 1;
	while(t--)
	{
        int n; cin >> n;

        queue<pair<ll,ll >> balls; 
        FOR(i, n){
            int w; cin >> w;
            if(w ==1)
            {
                int x, c; cin >> x >> c; 
                pair<ll,ll> temp(x,c);
                balls.push(temp);

            }else if( w == 2 )
            {
                ll c; cin >> c;
                ll sum = 0, count = 0;
                while (count < c)
                {
                    auto temp = balls.front();
                    count += temp.second;
                    //cout << "Count: " << count << "\n";
                    if(count <=  c){
                        sum += temp.first*temp.second;
                        balls.pop();
                    }else if(count > c)
                    {
                        //cout << "sum: " << sum << "\n";
                        //cout << "count: " << count << "\n";
                        //cout << "c: " << c << "\n";
                        sum += (temp.second - (count - c))*temp.first;
                        // cout << "sum: " << sum << "\n";
                        //count = c;
                        balls.front().second = (count - c);
                        //cout << (count - c)<< "\n";
                        //cout << "Acutual "<< balls.front().second <<"\n";
                        count = c;
                    }
                }
                cout <<  sum << "\n";
                
            }
        }

	}  

    return 0;
} 