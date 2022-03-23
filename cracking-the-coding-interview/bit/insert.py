def insert(n, m, i, j):
    ret = n
    ret &= -1 <<(j+1)
    ret |= m << i
    print(bin((1 << i )-1))
    ret |= n & ((1 << i) -1)
    return bin(ret)

def test():
    print(insert(0b100000000000, 0b10011, 2, 6 ))

if __name__ == "__main__":
    test()