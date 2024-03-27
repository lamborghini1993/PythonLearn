# -*- utf-8 -*-


def BubbleSort(lst):
    """冒泡排序 2N"""
    N = len(lst)
    for i in range(N):
        for j in range(i + 1, N):
            if lst[j] < lst[i]:
                lst[i], lst[j] = lst[j], lst[i]

    return lst


def QuickSort(lst):
    """快速排序 N*logN"""
    if len(lst) < 2:
        return lst
    midpivot = lst[0]
    lesspivot = [v for v in lst[1:] if v <= midpivot]
    greatpivot = [v for v in lst[1:] if v > midpivot]
    return QuickSort(lesspivot) + [midpivot] + QuickSort(greatpivot)


def SelectSort(lst):
    """选择排序"""
    N = len(lst)
    for i in range(N):
        mink = i
        for j in range(i + 1, N):
            if lst[j] < lst[mink]:
                mink = j
        if mink != i:
            lst[mink], lst[i] = lst[i], lst[mink]
    return lst


def ShellSort(lst):
    """希尔排序"""
    N = len(lst)
    gap = N // 2
    while gap > 0:
        for i in range(gap, N):
            tmp = lst[i]
            j = i
            while j >= gap and lst[j - gap] > tmp:
                lst[j] = lst[j - gap]
                j -= gap
            lst[j] = tmp
        gap //= 2
    return lst


def merge(left, right):
    result = []
    ln, rn = len(left), len(right)
    i = j = 0
    while i < ln and j < rn:
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    while i < ln:
        result.append(left[i])
        i += 1
    while j < rn:
        result.append(right[j])
        j += 1
    return result


def MergeSort(lst):
    """归并排序"""
    if len(lst) < 2:
        return lst
    mid = len(lst) // 2
    return merge(MergeSort(lst[:mid]), MergeSort(lst[mid:]))


def HeapSort(lst):
    """堆排序"""
    N = len(lst)

    def BuildHeap():
        for i in range(N >> 1, -1, -1):
            heapify(i)

    def heapify(i):
        left = 2 * i + 1
        right = left + 1
        largest = i
        if left < N and lst[left] > lst[largest]:
            largest = left
        if right < N and lst[right] > lst[largest]:
            largest = right
        if i != largest:
            lst[i], lst[largest] = lst[largest], lst[i]
            heapify(largest)

    BuildHeap()

    for i in range(N - 1, 0, -1):
        lst[i], lst[0] = lst[0], lst[i]
        N -= 1
        heapify(0)

    return lst


print(BubbleSort([2, 4, 6, 7, 1, 2, 5]))
print(QuickSort([2, 4, 6, 7, 1, 2, 5]))
print(SelectSort([2, 4, 6, 7, 1, 2, 5]))
# print(ShellSort([9, 1, 2, 5, 7, 4, 8, 6, 3, 5]))
print(ShellSort([2, 4, 6, 7, 1, 2, 5]))
print(MergeSort([2, 4, 6, 7, 1, 2, 5]))
# print(HeapSort([1, 3, 4, 5, 2, 6, 9, 7, 8, 0]))
print(HeapSort([2, 4, 6, 7, 1, 2, 5]))
