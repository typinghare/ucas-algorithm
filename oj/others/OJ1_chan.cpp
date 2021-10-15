////
//// Created by 潘榕 on 2021/10/15.
////
//
//#include <iostream>
//#include <vector>
//
//using namespace ::std;
//
//int superPow(int a, vector<int> &b) {
//    int numB = b[0];
//    a = a % 1337;
//    if (a == 0) {
//        return 0;
//    }
//    for (int i = 1; i < b.size(); i++) {
//        numB = (numB * 10 + b[i]) % 1140;
//    }
//    numB += 1140;
//    int x = a;
//    for (int j = 0; j < numB; j++) {
//        x = x % 1337;
//        x *= a;
//    }
//    x /= a;
//    return x;
//}
//
//int main(int argc, char const *argv[]) {
//    int tmp;
//    // vector<int>b = {3};
//    vector<int> b;
//    int a;
//    cin >> a;
//    string strTest = "";
//    cin >> strTest;
//    // cout << strTest << endl;
//    int len = strTest.size();
//    for (int i = 1; i < len; i += 2) {
//        b.push_back(int(strTest[i] - '0'));
//    }
//    cout << superPow(a, b);
//    return 0;
//}