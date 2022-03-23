def count_bit(x):
    ret = 0
    while x > 0:
        if x%2 == 1:
            ret += 1
        x //= 2
    return ret

def bit_length(x):
    ret = 0
    while x > 0:
        ret += 1
        x //= 2
    return ret

def last_start_bit(x):
    ret = 0
    while x > 0:
        if x%2 == 1:
            break
        x //= 2
        ret += 1
    return ret

def upper_neighbor_num(x):
    if x == 0:
        return -1
    y = x
    c0, c1 = 0, 0
    while y > 0:
        if y%2 == 0:
            c0 += 1
        else:
            break
        y //= 2
    while y > 0:
        if y%2 == 1:
            c1 += 1
        else:
            break
        y //= 2
    if c0 + c1 == bit_length(x):
        ret = (1 << (c0+c1)) + (1 << (c1-1)) - 1
        return ret
    ret = x
    ret |= 1 << c0+c1
    ret &= (-1 << (c0+c1))
    ret |= (1 <<(c1-1)) - 1
    return ret

def udner_neighbor_num(x):
    return x

def test():
    x = 0
    print(f"{bin(udner_neighbor_num(x))=}, {bin(x)=}, {bin(upper_neighbor_num(x))=}")
    x = 6
    print(f"{bin(udner_neighbor_num(x))=}, {bin(x)=}, {bin(upper_neighbor_num(x))=}")
    x = 7
    print(f"{bin(udner_neighbor_num(x))=}, {bin(x)=}, {bin(upper_neighbor_num(x))=}")
    for x in range(100, 110):
        print(f"{bin(udner_neighbor_num(x))=}, {bin(x)=}, {bin(upper_neighbor_num(x))=}")
    # for x in range(100, 110):
    #     print(f"{bin(udner_neighbor_num(x))=}, {bin(x)=}, {bin(upper_neighbor_num(x))=}")

if __name__=="__main__":
    test()

