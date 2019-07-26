#include<iostream>
#include<unordered_map>
#include<vector>
 
using namespace std;
 
int main()
{
    int temp;
    // candyCount: peopleCount
    unordered_map<int,int> m;
 
    while(cin>>temp)
    {
        m[temp]++;
    }
 
    int res = 0;
    for(auto iter = m.begin(); iter != m.end(); iter++)
    {
        int val = iter->first;
        int num = iter->second;

        // candyCount > peopleCount 
        //
        while(num > val)
        {
            res += val+1;
            num = num - val -1;
        }

        if(num == 0)
            continue;
        else
            res += (val+1);
    }
    cout << res << endl;
}
