def estimate():
    for i in range(1, 100):
        print(f"{i=}, {i&(i-1) =}")

# consideration 1
# x & y == 0 ⇔ x and y 's bits are different
# iff 11...111 and 100..0000, because we have to delete the most significant bit.
# iff x is power of two.

if __name__=="__main__":
    estimate()