#include <iostream>
#include <bitset>
using namespace std;
int main()
{
    // int x=1;
    // int y=0;
    // int z=0;
    // printf("x=%d,y=%d,z=%d\n",x,y,z);
    // y=x++;
    // printf("x=%d,y=%d,z=%d\n",x,y,z);
    // z=++x;
    // printf("x=%d,y=%d,z=%d\n",x,y,z);
    /*
        x=1,y=0,z=0
        x=2,y=1,z=0
        x=3,y=1,z=3
    */

    // short x = -129;
    // short y = x << 1;
    // cout<<bitset<16>(x)<<endl;
    // cout<<bitset<16>(y)<<endl;
    // 按位取反
    int x = 0x7fffffff;
    int y = 0x71111111;
    cout << bitset<32>(x) << "x" << endl;   // 01111111111111111111111111111111
    // cout << bitset<32>(~x) << "~x" << endl; // 10000000000000000000000000000000
    cout << bitset<32>(y) << "y" << endl;   // 01110001000100010001000100010001
    // cout << bitset<32>(~y) << "~y" << endl; // 10001110111011101110111011101110
    cout << "按位异或,相同为0,不同为1:" << endl;
    cout << bitset<32>(x^y) << "x^y" << endl;
    cout << "按位或,有1则1:" << endl;
    cout << bitset<32>(x&y) << "x&y" << endl;
    int a=0;
    int b=1;
    cout << "三位运算符:"<<endl;
    cout << (a>b?true:false)<< endl;
    cout << (a<b?true:false)<< endl;


    

    return 0;
}