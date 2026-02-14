#include <iostream>
using namespace std;

void dfs(vector<int> &x, vector<int> &y, vector<int> &z, int n)
{
    if (n == 1)
    {
        z.push_back(x.back()); // x.back()返尾元素
        x.pop_back();
        return;
    }
    dfs(x, z, y, n - 1);
    z.push_back(x.back()); // x.back()返尾元素
    x.pop_back();
    dfs(y, x, z, n - 1);
}

void slove()
{
    int n;
    cin >> n;
    vector<int> x(n);
    vector<int> y;
    auto z=y;

    int i = 0;
    while (i < n)
        cin >> x[i++];

    
    dfs(x, y, z, x.size());

    for (int i = 0; i < n; i++)
        cout<<z[i]<<" \t";
    
}

int main()
{
    slove();

    return 0;
}