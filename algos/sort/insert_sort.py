def insertion_sort(arr):
    for i in range(1, len(arr)):
        # make a reverse iteration to order each element
        for j in range(i, 0, -1):
            if arr[j] < arr[j-1]:
                # swap
                arr[j-1], arr[j] = arr[j], arr[j-1]
            else:
                break

if __name__ == "__main__":
    from random import randint

    # worst case
    arr = list(range(9, -1, -1))
    print(arr, "->", end=' ')
    insertion_sort(arr)
    print(arr)
    # random case
    arr = []
    for i in range(10):
        arr.append(randint(0, 9))
    print(arr, "->", end=' ')
    insertion_sort(arr)
    print(arr)