def bit_conversion(x, y):
    ret = 0
    while x > 0 or y > 0:
        if x%2 != y%2:
            ret += 1
        x //= 2
        y //= 2
    return ret

def test():
    print(f"{bit_conversion(2,3)}")
    print(f"{bit_conversion(29,15)}")

if __name__=="__main__":
    test()