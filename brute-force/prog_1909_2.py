# 19.09.28

COL_CHESS = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
LEN_CHESS = len(COL_CHESS)

bishops1 = ['D5']
bishops2 = ['D5', 'E8', 'G2']

def can_move_to(r,c, dir):
    if dir=='ul':
        return 0<=r-1<LEN_CHESS and 0<=c-1<LEN_CHESS
    elif dir=='ur':
        return 0<=r-1<LEN_CHESS and 0<=c+1<LEN_CHESS
    elif dir=='dl':
        return 0<=r+1<LEN_CHESS and 0<=c-1<LEN_CHESS
    elif dir=='dr':    
        return 0<=r+1<LEN_CHESS and 0<=c+1<LEN_CHESS
    

def move_up_left(r,c, chess):
    while True:
        if can_move_to(r,c, 'ul'):
            r = r-1
            c = c-1
            if chess[r][c] == 0:
                chess[r][c] = 1
        else:
            break

def move_up_right(r,c, chess):
    while True:
        if can_move_to(r,c, 'ur'):
            r = r-1
            c = c+1
            if chess[r][c] == 0:
                chess[r][c] = 1
        else:
            break

def move_down_left(r,c, chess):
    while True:
        if can_move_to(r,c, 'dl'):
            r = r+1
            c = c-1
            if chess[r][c] == 0:
                chess[r][c] = 1
        else:
            break

def move_down_right(r,c, chess):
    while True:
        if can_move_to(r,c, 'dr'):
            r = r+1
            c = c+1
            if chess[r][c] == 0:
                chess[r][c] = 1
        else:
            break

def search_brute_forcely(r_init,c_init, chess):
    move_up_left(r_init,c_init, chess)
    move_up_right(r_init,c_init, chess)
    move_down_left(r_init,c_init, chess)
    move_down_right(r_init,c_init, chess)

def main(bishops):
    global COL_CHESS
    chess = [[0 for _ in range(LEN_CHESS)] for _ in range(LEN_CHESS)]
    
    # initialize
    loc_bishops = []
    for bishop in bishops:
        r = abs(int(bishop[1])-LEN_CHESS)
        c = COL_CHESS.index(bishop[0])
        loc_bishops.append((r,c))
        chess[r][c] = 1

    # search
    for r,c in loc_bishops:
        search_brute_forcely(r,c, chess)
    
    chess_flat = sum(chess, [])
    print(LEN_CHESS**2 - sum(chess_flat))

if __name__=='__main__':
    main(bishops1)
    main(bishops2)