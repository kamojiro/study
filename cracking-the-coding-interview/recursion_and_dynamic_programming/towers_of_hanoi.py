def main():
    n = int(input())
    towers = [[ i for i in reversed(range(1, n+1))], [], []]
    def move_towers(p, i, j):
        if p == 1:
            x = towers[i].pop()
            towers[j].append(x)
            print(towers)
            return
        move_towers(p-1, i, 3^i^j)
        x = towers[i].pop()
        towers[j].append(x)
        print(towers)
        move_towers(p-1, 3^i^j, j)
    print(towers)
    move_towers(n, 0, 2)
if __name__=="__main__":
    main()