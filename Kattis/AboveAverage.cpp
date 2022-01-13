#include <iostream>
#include <string>
#include <iomanip>
using namespace std;

int main()
{
    int testCases;
    cin >> testCases;

    int numberOfScores;
    for (int i = 0; i < testCases; i++)
    {
        cin >> numberOfScores;

        int temp;
        int arr[numberOfScores];
        int total = 0;

        for (int j = 0; j < numberOfScores; j++)
        {
            cin >> temp;
            arr[j] = temp;
            total += temp;
            // cout << arr[j] << "arr\n";
        }
        // cout << total << "total\n";
        float avrage = total / numberOfScores;
        int scoresAboveAvrage = 0;

        for (int j = 0; j < numberOfScores; j++)
        {
            if (arr[j] > avrage)
            {
                scoresAboveAvrage++;
            }
        }

        // cout << scoresAboveAvrage << "scores above avrage\n";
        // cout << numberOfScores << "number of scores\n";

        float percentageOfScoresAboveAverage = scoresAboveAvrage / (float)numberOfScores * 100;

        cout << fixed;
        cout << setprecision(3);
        cout << percentageOfScoresAboveAverage << '%' << endl;
    }
    return 0;
}