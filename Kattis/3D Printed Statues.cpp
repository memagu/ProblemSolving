#include <iostream>
int main()
{
    int numberOfStatues;
    std::cin >> numberOfStatues;
    int days = 1;
    for (int i = 1; i < numberOfStatues; i *= 2)
        days++;
    std::cout << days;
}