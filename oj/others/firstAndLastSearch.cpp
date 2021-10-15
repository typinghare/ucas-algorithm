//#include <iostream>
//#include <stdio.h>
//
//using namespace std;
//
//const int maxLengh = 1e5;
//int inputArray[maxLengh];
//int targetArray[maxLengh];
//
//int find_loc(int left, int right, int target, int type) {
//    int mid_loc;
//    while (left <= right) {
//        mid_loc = (left + right) / 2;
//        if (inputArray[mid_loc] < target) {
//            left = mid_loc + 1;
//        } else if (inputArray[mid_loc] > target) {
//            right = mid_loc - 1;
//        } else if (inputArray[mid_loc] == target) {
//            if (type == 0) {
//                right = mid_loc - 1;
//            } else {
//                left = mid_loc + 1;
//            }
//        }
//    }
//
//    int final_loc;
//    if (type == 0) {
//        final_loc = right + 1;
//    } else {
//        final_loc = left - 1;
//    }
//
//    if (inputArray[final_loc] != target) {
//        return -1;
//    } else {
//        return final_loc;
//    }
//
//}
//
//
//int main() {
//
//    int arrayLen, targetLen;
//    scanf("%d%d", &arrayLen, &targetLen);
//
//    for (int i = 0; i < arrayLen; ++i) {
//        scanf("%d", &inputArray[i]);
//    }
//
//    for (int i = 0; i < targetLen; ++i) {
//        scanf("%d", &targetArray[i]);
//    }
//
//    for (int i = 0; i < targetLen; ++i) {
//        int left = 0;
//        int right = arrayLen - 1;
//        int left_loc = find_loc(left, right, targetArray[i], 0);
//        int right_loc = find_loc(left, right, targetArray[i], 1);
//        printf("%d %d\n", left_loc, right_loc);
//    }
//    return 0;
//}