def main():
    r, c = map(int, input().split())
    m = int(input())
    obstacles = [ tuple(map(lambda x: int(x)-1, input().split())) for _ in range(m)]
    grid = [[True]*c for _ in range(r)]
    for x, y in obstacles:
        grid[x][y] = False
    path = [(0, 0)]
    def search_path(x, y):
        if x+1 < r:
            if grid[x+1][y]:
                path.append((x+1, y))
                if (x+1, y) == (r-1, c-1):
                    return True
                if search_path(x+1, y):
                    return True
                else:
                    path.pop()
        if y+1 < c:
            if grid[x][y+1]:
                path.append((x, y+1))
                if (x, y+1) == (r-1, c-1):
                    return True
                if search_path(x, y+1):
                    return True
                else:
                    path.pop()
        return False
    if search_path(0, 0):
        print(path)
    else:
        print("Impossible")

if __name__=="__main__":
    main()