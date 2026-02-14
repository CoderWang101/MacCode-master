/*
小蓝准备去星际旅行，出发前想在本星系采购一些零食，
星系内有n.颗星球，由n—1条航路连接为连通图，第i颗星球卖第c种零食特产。
小蓝想出了 q个采购方案，第i个方案的起点为星球8i，终点为星球t，对于每种采购方案，小蓝将从起点走最短的航路到终点，
并且可以购买所有经过的星球上的零食（包括起点终点），请计算每种采购方案最多能买多少种不同的零食。
*/

#include<iostream>
#include<vector>
#include<queue>
using namespace std;


void bfs(vector<vector<int> > &graph,pair<int,int> pos)
{
    queue<int> q;
    int x=pos.first, y=pos.second;
    q.push(x);
    vector<int> visited(graph.size(),0);
    visited[x]=1;
    int count=0;
    while(!q.empty())
    {
        int cur=q.front();
        q.pop();
        count++;
        for(int i=1;i<graph.size();++i)
        {
            if(graph[cur][i]==1&&visited[i]==0)
            {
                visited[i]=1;
                q.push(i);
            }
        }
    }
    cout<<count<<endl;



    //bfs
    // queue<int> q;
    // q.push(pos_a);
    // vector<int> visited(graph.size(),0);
    // visited[pos_a]=1;
    // int count=0;
    // while(!q.empty())
    // {
    //     int cur=q.front();
    //     q.pop();
    //     count++;
    //     for(int i=1;i<graph.size();++i)
    //     {
    //         if(graph[cur][i]==1&&visited[i]==0)
    //         {
    //             visited[i]=1;
    //             q.push(i);
    //         }
    //     }
    // }
    // cout<<count<<endl;
}

int main()
{
    int n=0;//星球数
    int q=0;//采购方案数

    cin>>n>>q;
    int c[n+1];//星球上的零食种类
    for(int i=1;i<=n;++i)
        cin>>c[i];

    //路径图
    vector<vector<int> > graph(n+1,vector<int>(n+1,0));
    for(int i=0;i<n-1;++i)
    {
        int a,b;
        cin>>a>>b;
        graph[a][b]=1;
        graph[b][a]=1;
    }
    
    //采购方案
    pair<int,int> pos[q];
    for(int i=1;i<=q-1;++i)
    {
        int a,b;
        cin>>a>>b;
        pos[i]=make_pair(a,b);
    }

    //计算每种采购方案最多能买多少种不同的零食
    for(int i=1;i<=q-1;++i)
    {
        bfs(graph,pos[i]);
    }

    return 0;
}