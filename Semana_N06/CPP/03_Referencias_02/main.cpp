#include <iostream>

using namespace std;

void modifica(int *p)
{
    *p = 4;
}

void modifica2(int &r)
{
    r = 5;
}

int main()
{
    int x = 0;
    modifica(&x);
    cout << x << endl;
    return 0;
}
