def helper_pascal(n, row):
    # starts at row 0
    if len(row) > n:
        return row
    nr = [1]
    for i in range(len(row)-1):
        nr.append(row[i] + row[i+1])
    nr.append(1)
    return helper_pascal(n, nr)

def recursive_pascal(n):
    "Returns the nth row of the Pascal triangle."
    if n < 0:
        raise ValueError("The number of rows must be positive!")
    else:
        return helper_pascal(n, [1])

if __name__ == "__main__":
    for i in range(10):
        print(recursive_pascal(i))