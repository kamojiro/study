def main():
    n = int(input())
    for i in range(n//25):
        m = n - 25*i
        for j in range(m//10):
            l = m - j*10
            for k in range(l//5):
                print(f"25 cent: {i}, 10 cent: {j}, 5 cent: {k}, 1 cent: {l - k*5}")
if __name__=="__main__":
    main()