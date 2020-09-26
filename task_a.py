from math import sqrt

def function(arg, const):
    return arg ** 2 + sqrt(arg) - const

def root(left, right, eps, const):
    while right - left >= eps:
        x = (left + right) / 2
        if function(x, const) > 0:
            right = x
        else:
            left = x
    return (left + right) / 2


def solve():
    const = float(input())
    print(round(root(0, 10**11, 0.000001, const), 6))
    
    

if __name__ == "__main__":
    solve()