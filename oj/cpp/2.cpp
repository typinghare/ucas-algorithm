//#include <iostream>
//#include <vector>
//
//std::vector<int> solve(std::vector<int> nums, int target) {
//    if (nums.size() == 0) return std::vector<int>{-1, -1};
//
//    // find one target number (BS)
//    int l = 0, r = nums.size() - 1, mid;
//    while (l < r) {
//        mid = (l + r) >> 1;
//        if (nums[mid] == target) break;
//        if (nums[mid] > target) r = mid - 1;
//        else l = mid + 1;
//    }
//    mid = (r + l) >> 1;
//    if (mid < 0 || nums[mid] != target) return std::vector<int>{-1, -1};
//
//    // extend from both sides
//    int fix = mid, starting, ending;
//
//    // 1. starting on the left
//    l = 0, r = fix;
//    while (l < r) {
//        mid = (r + l) >> 1;
//        if (nums[mid] != target) l = mid + 1;
//        else r = mid;
//    }
//    starting = r;
//
//    // 2. ending on the right
//    l = fix, r = nums.size() - 1;
//    while (l < r) {
//        mid = (r + l + 1) >> 1;
//        if (nums[mid] != target) r = mid - 1;
//        else l = mid;
//    }
//    ending = r;
//    return std::vector<int>{starting, ending};
//}
//
////int main() {
////    // line 1
////    int n, m;
////    std::cin >> n;
////    std::cin >> m;
////
////    // line 2
////    std::vector<int> nums;
////    for (int i = 0; i < n; ++i) {
////        int a;
////        std::cin >> a;
////        nums.push_back(a);
////    }
////
////    // targets
////    for (int i = 0; i < m; ++i) {
////        int target;
////        std::cin >> target;
////        std::vector<int> result = solve(nums, target);
////        std::cout << result[0] << " " << result[1] << std::endl;
////    }
////
////    return 0;
////}