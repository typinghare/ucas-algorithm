# Divde and Conquer

## 知识归纳

#### 基本思想

将规模为N的问题分解为k个相互独立的子问题，这些子问题与原问题类型相同；将这些子问题再次分解成若干个独立的子问题，直至子问题的规模足够小；当子问题规模足够小后，对问题进行求解，再将解合并为原问题的解。

用分治求解问题是通常用递归的方式，因为递归型比较清晰。但实际上任何的递归都可以转化为迭代的形式，而且任何算法的递归型的开销都比迭代型要高（额外的开销来自于调用栈）。

#### 适用分治法求解的问题的特征

1. **自顶向下求解** - 该问题的规模缩小到一定程度时可以轻易地解决。
2. **最优子结构性质** - 该问题可以分解为若干个规模较小的相同问题。
3. **子问题合并求解** - 利用该问题分解出的子问题的解可以合并为该问题的解。
4. **子问题相互独立性** - 该问题所分解出的各个子问题是相互独立的，即子问题之间不包含公共的子问题。

### 分治法求解问题的步骤

1. **分解 (divide)**：将原问题分解成若干个规模较小，相互独立，与原问题形式相同的子问题。
2. **解决 (conquer)**：若子问题规模较小而容易被解决则直接解，否则递归地解各个子问题。
3. **合并 (merge)**：将各个子问题的解合并为原问题的解。

### Master Theorem (主定理)

在分治中，若一个规模为 $n$ 的实例归约成 $a$ 个子实例，每个子实例规模都相同（设为 $\frac{n}{b}$），则时间复杂度 $T(n)$ 可表示为：
$$
\begin{equation}
    T(n)=
    \begin{cases}
    	1 & \text{if}~n=1\\
    	aT(\frac{n}{b})+O(n^d) & \text{otherwise}
    \end{cases}
\end{equation}
$$
其中 $a>1$, $b>1$, $d>0$. 则 $T(n)$ 的上界可表示为：

1. 当 $d<log_ba$ 时，有$T(n)=O(n^{log_ba})$;
2. 当 $d=log_ba$ 时，有$T(n)=O(n^{log_ba}logn)$;
3. 当 $d>log_ba$ 时，有$T(n)=O(n^d)$.

在主定理中，$O(n^d)$ 为将 $a$ 个子问题的解合并的时间复杂度，即**分解**与**合并**这两步的合时间复杂度，一般**分解**的时间复杂度为$O(1)$，所以这里还是主要看$合并$的时间复杂度。

## 作业

### 1. k最大问题

[Leetcode 215: Kth Largest Element in an Array](https://leetcode.com/problems/kth-largest-element-in-an-array/)

可以采用类似快排的方法，在数组中随机选择一个数作为`pivot`，然后将数组中小于`pivot`的数放在其的左边（左部），大于或等于`pivot`的数放在其右边（右部），然后分以下三种情况：

1. 如果右部元素个数大于 $k$，则继续在右部中寻找第 $k$ 大的数；
2. 如果右部数量恰好等于$k-1$，则`pivot`就是所求值；
3. 否则：在左部中寻找第 $k-x-1$ 大的数，其中 $x$ 为右部元素个数，1代表`pivot`。

当 `low=high` 时进行解决，返回对应的数。（此处可以进行优化：当出现 `k=high-low+1` 时进行解决，返回指定区间中最小的数）

### 2. 二叉树问题



### 3. 最大连续子序列和问题

[Leetcode 53: Maximum Subarray](https://leetcode.com/problems/maximum-subarray/)

### 4. 目标值区间问题

[Leetcode 34: Find First and Last Position of Element in Sorted Array](https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/)

### 5. 多边形分解问题

这题就一条公式的事情：
$$

$$

### 6. 链表合并问题

[Leetcode 23: Merge k Sorted Lists](https://leetcode.com/problems/merge-k-sorted-lists/)

