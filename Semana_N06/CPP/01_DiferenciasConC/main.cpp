#include <iostream>

using namespace std;

int main()
{
    int i;
    for (i=0; i < 10; ++i)
        cout << i << endl;

    char nombre[50], apellido1[50], apellido2[50];
    cout << "Nombre?: ";
    cin >> nombre>> apellido1 >> apellido2;
    cout << nombre << ' ' << apellido1 << ' ' << apellido2 << endl;

    return 0;
}
