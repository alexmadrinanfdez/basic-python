def recursive_bin_search (arr, l, r, x):
    'Returns index of x in arr if present, else -1.'

    if hi >= lo:
        mid = lo + (hi - lo)/2
        # if element is present at the middle itself
        if arr[mid] == x:
            return mid
        # if element is smaller than mid, then it
        # can only be present in left subarray
        elif arr[mid] > x:
            return binarySearch(arr, lo, mid-1, x)
        # else the element can only be present
        # in right subarray
        else:
            return binarySearch(arr, mid + 1, hi, x)
        
    else:
        # element is not present in the array 
        return -1

def binary_search(arr, x):
    """
    :type nums: List[int]
    :type target: int
    :rtype: int
    """
    lo, hi = 0, len(arr) - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        if arr[mid] == x:
            return mid
        elif arr[mid] < x:
            lo = mid + 1
        else:
            hi = mid - 1
    
    return -1

if __name__ == "__main__":
    arr = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    assert binary_search(arr, 0) == 0
    assert binary_search(arr, 3) == 3
    assert binary_search(arr, 9) == 9
    assert binary_search(arr, 11) == -1