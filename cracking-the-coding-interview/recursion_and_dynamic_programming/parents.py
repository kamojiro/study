def main():
    n = int(input())
    dp = [[] for _ in range(n+1)]
    dp[0].append("")
    for i in range(n):
        ss = set()
        for s in dp[i]:
           ss.add("(" + s + ")")
        for j in range(i):
            for s in dp[j+1]:
                for t in dp[i-j]:
                    ss.add(s+t)
        dp[i+1] = list(ss)
    print(sorted(dp[-1]))
    print(len(dp[-1]))

if __name__=="__main__":
    main()