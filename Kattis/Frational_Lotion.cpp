#include <iostream>

int main() {
    while (true) {
        try {
            std::string s;
            std::cin >> s;
            std::size_t pos = s.find("/");
            int n = stoi(s.substr(pos+1));
            int temp = 0;

            for (int x = n + 1; x < n * 2 + 1; x++) {
                int numerator = x - n;
                int denominator = x * n;
                if (denominator % numerator == 0) {
                    temp++;
                }
            }
            std::cout << temp << std::endl;   
        }
        catch(const std::exception& e) {
            break;
        }
    }
    return 0;
}