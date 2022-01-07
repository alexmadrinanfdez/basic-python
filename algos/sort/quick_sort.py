from random import shuffle

def _partition(arr, lo, hi):
    pivot = lo
    # partition
    for i in range(lo+1, hi+1):
        if arr[i] < arr[lo]:
            # swap and advance pivot position
            arr[pivot+1], arr[i] = arr[i], arr[pivot+1]
            pivot += 1
    # update the pivot with its value
    arr[lo], arr[pivot] = arr[pivot], arr[lo]
    return pivot

def _sort(arr, lo, hi):
    if lo < hi:
        pivot = _partition(arr, lo, hi)
        # sort each partition separatedly
        # pivot is already sorted
        _sort(arr, lo, pivot-1)
        _sort(arr, pivot+1, hi)

def quicksort(arr):
    shuffle(arr) # avoid worst case
    _sort(arr, 0, len(arr)-1)

if __name__ == "__main__":
    from random import randint

    # worst case
    arr = list(range(9, -1, -1))
    print(arr, "->", end=' ')
    quicksort(arr)
    print(arr)
    # random case
    arr = []
    for i in range(10):
        arr.append(randint(0, 9))
    print(arr, "->", end=' ')
    quicksort(arr)
    print(arr)