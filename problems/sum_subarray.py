def num_subarr_sum(arr, k):
    """
    Returns the number of subarrays
    that sum up less or equal to 'k'
    """
    n = 0
    # sliding window
    tot = 0
    beg = -1
    for end in range(len(arr)):
        tot += arr[end]
        # shorten subarray until it meets condition
        while tot > k:
            beg += 1
            tot -= arr[beg]
        # if the subarray sums equal or less than the target, 
        # every subarray of itself does too
        n += end - beg
    return n

def max_subarr_sum(arr):
    "Returns the value of the maximum subarray sum"
    res = float("-inf")
    tmp = 0
    for num in arr:
        tmp += num
        res = max(res, tmp)
        tmp = max(tmp, 0)
    
    return res

if __name__ == "__main__":
    arr = [-2,1,-3,4,-1,2,1,-5,4]
    print(arr)
    print("Maximum subarray sum:", max_subarr_sum(arr))
    print("Number of subarrays summing at most 0:", num_subarr_sum(arr, 0))