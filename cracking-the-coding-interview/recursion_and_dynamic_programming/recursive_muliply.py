def main():
    a, b = map(int, input().split())
    if b == 0:
        return 0
    powers = []
    while b > 0:
        powers.append(b%2)
        b //= 2
    ans = a
    for x in reversed(powers[:-1]):
        ans <<= 1
        if x == 1:
            ans += a
    print(ans)
if __name__=="__main__":
    main()