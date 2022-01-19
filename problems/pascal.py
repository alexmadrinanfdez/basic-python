def helper_pascal(n, row):
    # starts at row 0
    if len(row) > n:
        return row
    # the first...
    nr = [1]
    for i in range(len(row)-1):
        nr.append(row[i] + row[i+1])
    # ...and last row elements are one
    nr.append(1)
    return helper_pascal(n, nr)

def recursive_pascal(n):
    "Returns the nth row of the Pascal triangle."
    if n < 0:
        raise ValueError("The number of rows must be positive!")
    else:
        return helper_pascal(n, [1])

def pascal(n):
    "Returns the first 'n' rows of Pascal's triangle."
    if n < 0:
        raise ValueError("The number of rows must be positive!")
    triag = []
    for i in range(n):
        # starts at row 0
        row = [None for _ in range(i+1)]
        # the first and last row elements are one
        row[0], row[-1] = 1, 1
        for j in range(1, i):
            row[j] = triag[i-1][j-1] + triag[i-1][j]
        triag.append(row)
    return triag

if __name__ == "__main__":
    triangle = pascal(10)
    for row in triangle:
        print(row)