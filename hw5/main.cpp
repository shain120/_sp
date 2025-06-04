#include <iostream>
#include <cmath> 
using namespace std;

int power(int a, int b)
{
    int re = 1;
    for(int i=0;i<b;i++){
        re *= a;
    }
    return re;
}
int main()
{
    cout<<"result:"<<power(5,3);
}