#include <iostream>
#include <string>
using namespace std;
int main()
{
    string strIn;
    cin >> strIn;
    int A = 0;
    int B = 0;

    for (int i = 0; i < strIn.length(); i += 2)
    {
        if (strIn[i] == 'A')
        {
            A += (int)strIn[i + 1] - 48;
        }
        else
        {
            B += (int)strIn[i + 1] - 48;
        }
    }

    if (A > B)
    {
        cout << "A\n";
    }
    else
    {
        cout << "B\n";
    }
    return 0;
}