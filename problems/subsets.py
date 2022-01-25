def subsets(nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if len(nums) == 0:
            return [[]]
        return  [[nums[0]] + x for x in subsets(nums[1:])] + [x for x in subsets(nums[1:])]

def power_set(S):
    # N stores the total number of subsets
    N = 2 ** len(S)
    s = set()
    # for duplicates
    S.sort()

    for i in range(N):
        subset = []
        # check every bit of i
        for j in range(len(S)):
            # if j'th bit of i is set, append S[j] to the subset
            if i & (1 << j):
                subset.append(S[j])
        # insert the subset as a hashable object
        s.add(tuple(subset))
    
    return s

if __name__ == "__main__":
    ss = subsets(range(5))
    ps = power_set(list(range(5)))
    # because input has no duplicates
    assert len(ss) == len(ps)
    
    superset = ['a', 'b', 'a']
    ss = subsets(superset)
    ps = power_set(superset)
    # because input contains duplicates
    assert len(ss) != len(ps)

    print(superset)
    print("Power set:", ps)
    print("All subsets:", ss)