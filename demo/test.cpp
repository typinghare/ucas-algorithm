////
//// Created by James on 2021/10/15.
////
//
//#include <iostream>
//#include <algorithm>
//
//using namespace std;
//
//int main() {
//    int a[14] = {1, 1, 2, 3, 5, 5, 5, 6, 7, 7, 7, 8, 8, 9};
//    int target = 5;
//    int *lower = lower_bound(a, a + 13, target);
//    int *upper = upper_bound(a, a + 13, target);
//    std::cout << "lower bound: " << lower - a << std::endl;
//    std::cout << "upper bound: " << upper - a - 1 << std::endl;
//    return 0;
//}