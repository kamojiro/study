def main():
    characters = list(input())
    n = len(characters)
    used = [False]*n
    x = []
    def permutaion_without_dups(c, n):
        if c == n:
            print("".join(x))
            return
        for i in range(n):
            if not used[i]:
                x.append(characters[i])
                used[i] = True
                permutaion_without_dups(c+1, n)
                x.pop()
                used[i] = False
    permutaion_without_dups(0, n)
if __name__=="__main__":
    main()