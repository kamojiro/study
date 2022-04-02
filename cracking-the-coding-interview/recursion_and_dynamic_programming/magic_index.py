def main():
    #enough  O(N)?, bacause the length of this array is N
    N = int(input())
    A = list(map(int, input().split()))
    for i, a in enumerate(A):
        if i == a:
            print(a)
if __name__=="__main__":
    main()