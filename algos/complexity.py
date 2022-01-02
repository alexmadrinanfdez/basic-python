import time

# Algorithmic analysis (run time and memory allocation)
# Common orders of growth:

# Constant: O(1)
def const_runtime(N):
    cnt = 0
    cnt += 1
    return cnt

# Logarithmic: O(log N)
def log_runtime(N):
    cnt = 0
    while N > 0:
        N //= 2
        cnt += 1
    return cnt

# Linear: O(N)
def lin_runtime(N):
    cnt = 0
    for i in range(N):
        cnt += 1
    return cnt

# Linearithmic (or log-linear): O(Nlog N)
def nlog_runtime(N):
    cnt = 0
    for i in range(N):
        while i > 0:
            i //= 2
            cnt += 1
    return cnt

# Polynomial: O(N^C) -> quadratic: O(N^2)
def quad_runtime(N):
    cnt = 0
    for i in range(N):
        for j in range(N):
            cnt += 1
    return cnt

# Exponential: O(C^N) -> base two: O(2^N)
def exp_runtime(N):
    if N == 0:
        return 1
    else:
        return exp_runtime(N-1) + exp_runtime(N-1)

if __name__ == "__main__":
    const_op = []; const_t = []
    log_op = []; log_t = []
    lin_op = []; lin_t = []
    nlog_op = []; nlog_t = []
    quad_op = []; quad_t = []
    exp_op = []; exp_t = []

    for i in range(5):
        N = 2 ** i

        start = time.time()
        op = const_runtime(N)
        end = time.time()
        const_op.append(op)
        const_t.append(end - start)

        start = time.time()
        op = log_runtime(N)
        end = time.time()
        log_op.append(op)
        log_t.append(end - start)

        start = time.time()
        op = lin_runtime(N)
        end = time.time()
        lin_op.append(op)
        lin_t.append(end - start)

        start = time.time()
        op = nlog_runtime(N)
        end = time.time()
        nlog_op.append(op)
        nlog_t.append(end - start)

        start = time.time()
        op = quad_runtime(N)
        end = time.time()
        quad_op.append(op)
        quad_t.append(end - start)

        start = time.time()
        op = exp_runtime(N)
        end = time.time()
        exp_op.append(op)
        exp_t.append(end - start)
    
    print("Number of operations per order of growth")
    print("\t- Constant:", const_op)
    print("\t- Logarithmic:", log_op)
    print("\t- Linear:", lin_op)
    print("\t- Linearithmic:", nlog_op)
    print("\t- Quadratic:", quad_op)
    print("\t- Exponential:", exp_op)

    print("Run time per order of growth")
    print("\t- Constant:", const_t)
    print("\t- Logarithmic:", log_t)
    print("\t- Linear:", lin_t)
    print("\t- Linearithmic:", nlog_t)
    print("\t- Quadratic:", quad_t)
    print("\t- Exponential:", exp_t)