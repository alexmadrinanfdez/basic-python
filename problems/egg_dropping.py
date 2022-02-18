def drops_recursive(n, f):
    if n == 0 or n == 1 or f == 1:
        return n
    
    res = float("inf")
    for i in range(n):
        i += 1
        # look for the minimum tries in the worst case
        res = min(res, 1 + max(
            drops_recursive(i-1, f-1), # egg breaks
            drops_recursive(n-i, f)    # success
        ))
    return res

def drops_iterative(n, f):
    dp = [[float("inf") for _ in range(f+1)] for _ in range(n+1)]
    # base cases
    for i in range(1, n+1):
        dp[i][1] = i
    for j in range(1, f+1):
        dp[0][j] = 0
        dp[1][j] = 1
    
    for i in range(2, n+1):
        for j in range(2, f+1):
            res = float("inf")
            for k in range(1, i+1):
                res = min(res, 1 + max(dp[k-1][j-1], dp[i-k][j]))
            dp[i][j] = res
    return dp[-1][-1]

def drops(n, f):
    # https://brilliant.org/wiki/egg-dropping/
    pass

if __name__ == "__main__":
    assert drops_recursive(10, 2) == 4
    assert drops_iterative(25, 2) == 7