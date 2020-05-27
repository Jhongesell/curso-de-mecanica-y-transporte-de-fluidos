#include <iostream>

using namespace std;

int main()
{
    /*int x, *p; // *p: puntero
    p = &x;
    *p = 5;
    cout << x << endl;*/

    int x;
    int &r = x; // &r : es una referencia
    r = 5;
    cout << x << endl;


    return 0;
}
