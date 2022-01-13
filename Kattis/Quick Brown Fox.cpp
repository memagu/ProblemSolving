#include <iostream>
#include <string>
#include <set>
#include <vector>
#include <algorithm>
using namespace std;

int main()
{
    int numberOfStrings;
    cin >> numberOfStrings;
    string strIn;
    getline(cin, strIn);

    for (int i = 0; i < (numberOfStrings); i++)
    {
        set<char> alphabet{'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'};
        getline(cin, strIn);
        set<char> hits{};

        for (char letter : strIn)
        {
            alphabet.erase(tolower(letter));
        }

        if (alphabet.size() == 0)
        {
            cout << "pangram\n";
        }
        else
        {
            cout << "missing ";
            for (auto j = alphabet.begin(); j != alphabet.end(); ++j)
            {
                std::cout << *j;
            }

            cout << '\n';
        }
    }
    return 0;
}
