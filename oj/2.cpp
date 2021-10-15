#include <iostream>
#include <string>

class Position {
public:
    int left;
    int right;

    Position(int left, int right) {
        this->left = left;
        this->right = right;
    }
};

Position solve(int *arr, int target, int l, int r) {
    if (r < 0) {
        return Position(-1, -1);
    }

    // conquer
    if (l == r) {
        // leaf node position
        return arr[r] == target ? Position(r, r) : Position(-1, -1);
    }

    // divide
    int m = (l + r) >> 1;
    Position left_result = arr[m] >= target ? solve(arr, target, l, m) : Position(-1, -1);
    Position right_result = arr[m + 1] <= target ? solve(arr, target, m + 1, r) : Position(-1, -1);

    // combine
    if (left_result.left == -1) {
        // in this case, left half does not contain target element.
        return right_result;
    } else {
        // in this case, left part contains at least one target element.
        return right_result.left == -1 ? left_result : Position(left_result.left, right_result.right);
    }
}

int main() {
    std::string line, str;

    // line 1
    int n, m;
    std::cin >> n;
    std::cin >> m;

    // line 2
    int *arr = new int[n];
    for (int i = 0; i < n; ++i) {
        std::cin >> arr[i];
    }

    // targets
    for (int i = 0; i < m; ++i) {
        int target;
        std::cin >> target;
        Position result = solve(arr, target, 0, n - 1);
        std::cout << result.left << " " << result.right << std::endl;
    }
}