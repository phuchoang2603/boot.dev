def factorial_r(x):
    if x == 0:
        return 1
    return x * factorial_r(x - 1)
