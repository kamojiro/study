def main():
    #enough  O(N)?, bacause the length of this array is N
    N = int(input())
    A = list(map(int, input().split()))
    for p in range(1<<N):
        set = []
        q = p
        for i in range(N):
            if q%2 == 1:
                set.append(A[i])
            q //= 2
        print(set)
if __name__=="__main__":
    main()