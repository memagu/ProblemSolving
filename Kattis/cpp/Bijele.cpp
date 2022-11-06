#include <iostream>
#include <string>
using namespace std;

int main()
{
    /*
    int numberOfPieces[] = {1, 1, 2, 2, 2, 8};
    string currentNumberOfPieces;
    getline(cin, currentNumberOfPieces);
    // cout << currentNumberOfPieces << "\n";

    for (int i = 0; i < 6; ++i) {
        int currentNumberOfPiece = currentNumberOfPieces[i*2] - 48;
        cout << numberOfPieces[i] - currentNumberOfPiece << " ";
    }
    */

    int k;
    int q;
    int r;
    int b;
    int n;
    int p;

    cin >> k >> q >> r >> b >> n >> p;
    cout << 1 - k << 1 - q << 2 - r << 2 - b << 2 - n << 8 - p;
}