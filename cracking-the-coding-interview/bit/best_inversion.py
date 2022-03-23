def best_inversion(x):
    ret = 0
    a, b = 0, 0
    count = 0
    while x > 0:
        if x%2 == 0:
            a, b = count, a
            count = 0
        else:
            count += 1
        x //= 2
        ret = max(ret, a+b+1)
    return ret

def test():
    x = 0b11101101101111
    print(f"{x=}, {best_inversion(x)=}")
    for i in range(111112, 111112+10):
        print(f"{bin(i)=}, {best_inversion(i)=}")

if __name__=="__main__":
    test()


