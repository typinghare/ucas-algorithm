//#include <iostream>
//#include <string>
//#include <vector>
//#include <math.h>
//
//int solve(int r, std::vector<int> b, int d) {
//    int length = b.size();
//
//    // conquer
//    if (length == 1 && b[0] == 1) {
//        return r;
//    }
//
//    // b /= 2
//    std::vector<int> half;
//    int carry;
//    if (b[0] == 1) {
//        carry = 1;
//    } else {
//        half.push_back(b[0] >> 1);
//        carry = b[0] & 1;
//    }
//    for (int i = 1; i < length; ++i) {
//        half.push_back((b[i] >> 1) + carry * 5);
//        carry = b[i] & 1;
//    }
//
//    // divide and combine
//    if (carry == 1) {
//        // odd
//        return int(pow(solve(r, half, d), 2) * r) % d;
//    } else {
//        // even
//        return int(pow(solve(r, half, d), 2)) % d;
//    }
//}
//
//int main() {
//    int d = 1337;       // divisor
//    int a;              // base number
//    std::string str;    // line 2
//
//    // input
//    std::cin >> a;
//    std::cin >> str;
//
//    // parse str, stores numbers to an array
//    str = str.substr(1, str.length() - 1);
//    std::vector<int> b;
//    for (int i = 0; i < str.length(); ++i) {
//        char ch = str[i];
//        if (ch >= 48 && ch <= 57) {
//            b.push_back(ch - 48);
//        }
//    }
//
//    std::cout << solve(a % d, b, d) << std::endl;
//}
