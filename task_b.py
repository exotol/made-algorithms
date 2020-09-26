def solve():
    width, height, count = map(int, input().split())
    left = 0
    right = max(width, height) * count
    while right > left + 1:
        mid = (left + right) // 2
        if (mid // height) * (mid // width) < count:
            left = mid
        else:
            right = mid
    print(right)
    

if __name__ == "__main__":
    solve()