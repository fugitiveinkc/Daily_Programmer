def is_n_in_fib(f1, n):
    a = 0
    b = f1
    while b < n:
        a, b = b, a + b
    return b == n


def find(target):
    f1 = 1
    while not is_n_in_fib(f1, target):
        f1 += 1
    return f1


print find(123456789)
