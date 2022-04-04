def main():
    d = dict()
    def countEval(t, r):
        if len(t) == 1:
            if int(t) == r:
                return 1
            else:
                return 0
        count = 0
        for i in range(1, len(t), 2):
            if (t[:i], 1) not in d:
                d[(t[:i], 1)] = countEval(t[:i], 1)
            if (t[i+1:], 1) not in d:
                d[(t[i+1:], 1)] = countEval(t[i+1:], 1)
            a = d[(t[:i], 1)]
            b = d[(t[i+1:], 1)]
            if (t[:i], 0) not in d:
                d[(t[:i], 0)] = countEval(t[:i], 0)
            if (t[i+1:], 0) not in d:
                d[(t[i+1:], 0)] = countEval(t[i+1:], 0)
            na = d[(t[:i], 0)]
            nb = d[(t[i+1:], 0)]
            if t[i] == "&":
                if r:
                    count += a*b
                else:
                    count += a*nb + na*b + na*nb
            elif t[i] == "|":
                if r:
                    count += a*b + a*nb + na*b
                else:
                    count += na*nb
            elif t[i] == "^":
                if r:
                    count += a*nb + na*b
                else:
                    count += a*b + na*nb
        return count
    s = input()
    z = int(input())
    print(countEval(s,z))

if __name__=="__main__":
    main()