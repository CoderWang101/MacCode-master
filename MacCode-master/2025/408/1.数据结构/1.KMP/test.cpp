#include <iostream>
#include <bitset>
#include <string>
using namespace std;

int Index_KMP(string S,string T,int next[])
{
    int i=1,j=1;
    while (i<=S.length()&&j<=T.length())
    {
        if (j==0||S[i]==T[j])
        {
            i++;
            j++;
        }
        else
        {
            j=next[j];
        }
    }
    if(j>T.length())
        return i-T.length();
    else
        return 0;
}

int main()
{    

    return 0;
}