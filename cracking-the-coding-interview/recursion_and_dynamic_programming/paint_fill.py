class UnionFindTree:
    def __init__(self, n) -> None:
        self.tree = [ i for i in range(n)]
    def find(self, x):
        p = self.tree[x]
        if p == x:
            return x
        a = self.tree[p]
        self.tree[x] = a
        return a

    def union(self, x, y):
        bx, by = self.find(x), self.find(y)
        if bx > by:
            bx, by = by, bx
        self.tree[y] = bx
        self.tree[x] = bx

def main():
    h, w = map(int, input().split())
    s = [list(input()) for _ in range(h)]
    x, y = map(int, input().split())
    color = input()
    union_find_tree = UnionFindTree(h*w)
    for i in range(h):
        for j in range(w):
            if i > 0:
                if s[i][j] == s[i-1][j]:
                    union_find_tree.union(i*w+j, (i-1)*w+j)
            if i < h-1:
                if s[i][j] == s[i+1][j]:
                    union_find_tree.union(i*w+j, (i+1)*w+j)
            if j > 0:
                if s[i][j] == s[i][j-1]:
                    union_find_tree.union(i*w+j, i*w+j-1)
            if j < w-1:
                if s[i][j] == s[i][j+1]:
                    union_find_tree.union(i*w+j, i*w+j+1)
    for i in range(h):
        for j in range(w):
            if union_find_tree.find(i*w+j) == union_find_tree.find(x*w+y):
                s[i][j] = color
    for i in range(h):
        print("".join(s[i]))
    
if __name__=="__main__":
    main()