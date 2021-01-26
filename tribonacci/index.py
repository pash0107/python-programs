def tribonacci(s, n):
    for c in range(n - 3):
        s += [s[c] + s[c+1] + s[c+2]]
        return s[0:n]

tribonacci([1, 1, 1], 10)