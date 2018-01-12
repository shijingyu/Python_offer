def leftDatas(a, d):
    return(a[d:]+a[:d])

if __name__ == "__main__":
    n, d = input().strip().split(' ')
    n, d = [int(n), int(d)]
    a = list(map(int, input().strip().split(' ')))
    result = leftDatas(a, d)
    print (" ".join(map(str, result)))