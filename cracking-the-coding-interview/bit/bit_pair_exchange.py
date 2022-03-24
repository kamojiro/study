def bit_pair_exchange(x):
    n = x.bit_length()//4+1
    even_mask = int("a"*n, 16)
    odd_mask = int("5"*n, 16)
    print(bin(even_mask), bin(odd_mask))
    return ((x & even_mask) >> 1) + ((x & odd_mask) << 1)
    

def test():
    x = 1000
    print(f"{bin(x)=}, {bin(bit_pair_exchange(x))}")

if __name__=="__main__":
    test()