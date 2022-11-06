#include <iostream>
#include <string>
#include <math.h>

int main() {
    int n, e;
    std::cin >> n >> e;
    std::string num;
    int hits = 0;

    for (int i = 1; i < n+1; i++) {
        num = std::to_string(i);
        if (num.find(std::to_string((int)pow(2, e))) != -1)
        {
            hits++;
        }
    }
    
    std::cout << hits;

    return 0;
}