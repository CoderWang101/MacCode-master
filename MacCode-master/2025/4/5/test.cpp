// #define _CRT_SECURE_NO_WARNINGS 
// #include <stdio.h>
#include <iostream>
using namespace std;
struct S1
{
	short x1;
	short x2;
}a;
 
int main()
{
	struct S1 s1;
 
	cout<<sizeof(s1)<<endl;//4
 
	return 0;
}