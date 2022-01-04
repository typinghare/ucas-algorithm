# [Job Schedule]
# There are n distinct jobs, labeled J1, J2, . . . , Jn, which can be performed completely independently
# of one another. Each job consists of two stages: first it needs to be preprocessed on
# the supercomputer, and then it needs to be finished on one of the PCs.
# Let’s say that job Ji needs pi seconds of time on the supercomputer, followed by fi seconds
# of time on a PC.
# Since there are at least n PCs available on the premises, the finishing of the jobs can be
# performed on PCs at the same time. However, the supercomputer can only work on a single
# job a time without any interruption. For every job, as soon as the preprocessing is done on the
# supercomputer, it can be handed off to a PC for finishing.
# Let’s say that a schedule is an ordering of the jobs for the supercomputer, and the completion
# time of the schedule is the earliest time at which all jobs have finished processing on the PCs.
# Give a polynomial-time algorithm that finds a schedule with as small a completion time as
# possible.

# see: https://stackoverflow.com/questions/10025616/scheduling-greedy-algorithm
# see: http://mypathtothe4.blogspot.com/2013/03/greedy-algorithm-example.html

from typing import List


def jobSchedule(p: List[int], f: List[int]):
    """
    :param f: seconds of time on the supercomputer
    :param p: seconds of time on the PCs
    :return: the minimum time
    """

    # Schedule the jobs on the supercomputer in decreasing order of desktop time.
    # Sort the array f of desktop computing times in decreasing order. For every swap made in f,
    # keep track of the ordering by swapping the same elements in p.

    # Apply quicksort(in-place) algorithm on f
    def qs(low: int, high: int):
        # recursion termination
        if low >= high:
            return

        # partition
        pivot = f[high]

        # swap two elements in p
        def swap(arr: list, i: int, j: int):
            temp = arr[i]
            arr[i] = arr[j]
            arr[j] = temp

        pi = low  # partition index
        for i in range(low, high):
            if f[i] < pivot:
                swap(f, pi, i)
                swap(p, pi, i)
                pi += 1
        swap(f, pi, high)
        swap(p, pi, high)

        # quicksort two parts
        qs(low, pi - 1)
        qs(pi + 1, high)

    # sort
    qs(0, len(f) - 1)


# TEST
p = [10, 3, 5, 7]
f = [2, 7, 9, 4]
jobSchedule(p, f)
print(p)
print(f)
