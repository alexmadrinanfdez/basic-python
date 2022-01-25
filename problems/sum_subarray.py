def num_subarr_sum(arr, k):
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

if __name__ == "__main__":
    nums = [1,2,3,0,3]
    target = 3
    print(num_subarr_sum(nums, target))