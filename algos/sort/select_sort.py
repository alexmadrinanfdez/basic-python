def selection_sort(arr):
    for i in range(len(arr)):
        # search for the minimum each iteration
        imin = i
        for j in range(i+1, len(arr)):
            if arr[j] < arr[imin]:
                imin = j
        # one swap per iteration
        arr[i], arr[imin] = arr[imin], arr[i]

if __name__ == "__main__":
    from random import randint

    # average case
    arr = list(range(9, -1, -1))
    print(arr, "->", end=' ')
    selection_sort(arr)
    print(arr)
    # random case
    arr = []
    for i in range(10):
        arr.append(randint(0, 9))
    print(arr, "->", end=' ')
    selection_sort(arr)
    print(arr)