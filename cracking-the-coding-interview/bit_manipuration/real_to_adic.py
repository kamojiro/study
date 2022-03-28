from ast import For
from cgi import MiniFieldStorage


def real_to_adic(x):
    # 0 <= x <= 1
    if x == 0:
        return "0"
    elif x == 1:
        return "1"
    ret = "0."
    for _ in range(31):
        x *= 2
        if x >= 1:
            ret += "1"
            x -= 1
        else:
            ret += "0"
        if x == 0:
            return ret
    return f"error, {ret=}"

def test():
    x = 1
    print(f"{x=}, {real_to_adic(x)}")
    x = 0
    print(f"{x=}, {real_to_adic(x)}")
    x = 0.25
    print(f"{x=}, {real_to_adic(x)}")
    x = 0.125
    print(f"{x=}, {real_to_adic(x)}")
    x = 0.375
    print(f"{x=}, {real_to_adic(x)}")
    x = 0.3
    print(f"{x=}, {real_to_adic(x)}")

if __name__ == "__main__":
    test()