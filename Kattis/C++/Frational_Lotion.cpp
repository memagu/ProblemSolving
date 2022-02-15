//#include <iostream>
//
//int main() {
//    while (true) {
//        try {
//            std::string s;
//            std::cin >> s;
//            std::size_t pos = s.find("/");
//            int n = stoi(s.substr(pos+1));
//            int temp = 0;
//
//            for (int x = n + 1; x < n * 2 + 1; x++) {
//                int numerator = x - n;
//                int denominator = x * n;
//                if (denominator % numerator == 0) {
//                    temp++;
//                }
//            }
//            std::cout << temp << std::endl;
//        }
//        catch(const std::exception& e) {
//            break;
//        }
//    }
//    return 0;
//}



#include <chrono>
using namespace std::chrono;

#include <iostream>

int main() {
    while (true) {
        try {
            auto start = high_resolution_clock::now();

            std::string s;
            std::cin >> s;
            int n = stoi(s.substr(2));
            int counter = 0;

            for (int x = n + 1; x < n * 2 + 1; x++) {
                if ((x * n) % (x - n) == 0) {
                    counter++;
                }
            }
            std::cout << counter << std::endl;

            auto stop = high_resolution_clock::now();
            auto duration = duration_cast<nanoseconds>(stop - start);
            std::cout << duration.count() << std::endl << std::endl;
        }
        catch(const std::exception& e) {
            break;
        }
    }
    return 0;
}