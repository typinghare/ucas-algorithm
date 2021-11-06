def quicksort(arr: list, low: int, high: int):
    # recursion termination
    if low >= high:
        return

    # partition
    pivot = arr[high]  # pivot can be any element in arr

    # swap two element in arr
    def swap(i, j):
        temp = arr[i]
        arr[i] = arr[j]
        arr[j] = temp

    pi = low  # partition index
    for i in range(low, high):
        if arr[i] < pivot:
            swap(pi, i)
            pi += 1
    swap(pi, high)

    # quicksort two parts
    quicksort(arr, low, pi - 1)  # before <pi>
    quicksort(arr, pi + 1, high)  # after <pi>


# Test
li = [10, 80, 30, 90, 40, 50, 70]
quicksort(li, 0, len(li) - 1)
