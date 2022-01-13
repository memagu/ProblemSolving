#include <iostream>
#include <string>
#include <set>
#include <map>
using namespace std;

int main()
{
    int numberOfApplications;
    cin >> numberOfApplications;
    string strIn;
    string fName;
    string lName;
    string fullNameAndCourse;
    set<string> names;
    string course;
    map<string, int> courses;

    for (int i = 0; i < numberOfApplications; i++)
    {
        cin >> fName >> lName >> course;
        fullNameAndCourse = fName + lName + course;
        if (names.find(fullNameAndCourse) == names.end())
        {
            courses[course]++;
        }
        names.insert(fullNameAndCourse);
    }

    for (const auto entry : courses)
    {
        cout << entry.first << " " << entry.second << endl;
    }

    return 0;
}
