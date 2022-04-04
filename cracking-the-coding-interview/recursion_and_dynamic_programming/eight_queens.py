import sys

sys.setrecursionlimit(10**6) 

def main():
    queens = []
    def search_queen():
        if len(queens) == 8:
            return True
        area = make_area(queens)
        for i in range(8):
            for j in range(8):
                if area[i][j]:
                    queens.append((i, j))
                else:
                    continue
                if search_queen():
                    return True
                else:
                    queens.pop()
    search_queen()
    board = [["."]*8 for _ in range(8)]
    for x, y in queens:
        board[x][y] = "&"
    for i in range(8):
        print("".join(board[i]))
def make_area(queens):
    board = [[True]*8 for _ in range(8)]
    for x, y in queens:
        for i in range(8):
            board[i][y] = False
            
        for j in range(8):
            board[x][j] = False
        for i in range(8):
            aj = i-(x-y)
            if 0 <= aj < 8:
                board[i][aj] = False
            bj = x+y-i
            if 0 <= bj < 8:
                board[i][bj] = False
    return board
        
if __name__=="__main__":
    main()