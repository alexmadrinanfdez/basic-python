def _merge(arr, lo, mi, hi):
    temp = arr[:] # copy, NOT reference
    i = lo
    j = mi+1
    # merge arr[lo, mid] and arr[mid+1, hi]
    for k in range(lo, hi+1):
        # both sublists are already sorted
        if i <= mi and j <= hi:
            if temp[i] <= temp[j]:
                arr[k] = temp[i]
                i += 1
            else:
                arr[k] = temp[j]
                j += 1
        # copy remaining elements
        elif i <= mi:
            arr[k] = temp[i]
            i += 1
        elif j <= hi:
            arr[k] = temp[j]
            j += 1

def _sort(arr, lo, hi):
    if lo < hi:
        mi = (lo + hi) // 2
        # sort by halves
        _sort(arr, lo, mi)
        _sort(arr, mi+1, hi)
        # merge in order
        _merge(arr, lo, mi, hi)

def mergesort(arr):
    _sort(arr, 0, len(arr)-1)

if __name__ == "__main__":
    from random import randint

    # worst case
    arr = list(range(9, -1, -1))
    print(arr, "->", end=' ')
    mergesort(arr)
    print(arr)
    # random case
    arr = []
    for i in range(10):
        arr.append(randint(0, 9))
    print(arr, "->", end=' ')
    mergesort(arr)
    print(arr)