def main():
    n = int(input())
    dp = [0]*(n+1)
    dp[0] = 1
    for i in range(n):
        if i+1 <= n:
            dp[i+1] += dp[i]
        if i+2 <= n:
            dp[i+2] += dp[i]
        if i+3 <= n:
            dp[i+3] += dp[i]
    print(dp[n])

if __name__=="__main__":
    main()