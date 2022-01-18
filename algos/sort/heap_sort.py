from ...data_structs import heap

def heap_sort(arr):
    pq = heap.PriorityQueue()
    for e in arr:
        pq.insert(e)
    i = len(arr) - 1
    while not pq.empty():
        arr[i] = pq.del_max()
        i -= 1

if __name__ == "__main__":
    from random import randint

    # average case
    arr = list(range(9, -1, -1))
    print(arr, "->", end=' ')
    heap_sort(arr)
    print(arr)
    # random case
    arr = []
    for i in range(10):
        arr.append(randint(0, 9))
    print(arr, "->", end=' ')
    heap_sort(arr)
    print(arr)