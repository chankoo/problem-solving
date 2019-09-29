# 19.09.30

# 사탕 획득 카드게임
# - 플레이어: 참가자
# - 팔로워: 특정 플레이가 사탕 획득시 같이 사탕을 받는 플레이어
# 플레이어가 순서대로 카드를 뽑는다. 카드를 모두 뽑았을때 플레이어 각각의 획득 사탕 개수를 출력한다
#
# - 카드: {A, J, Q, K} 4종류의 카드
#     - A: 카드뽑은 플레이어가 사탕을 획득(팔로워에 전파)
#     - J: 카드뽑은 플레이어의 양옆 플레이어가 사탕을 획득(팔로워에 전파)
#     - Q: 모든 플레이어가 사탕을 획득(팔로워에게 전파되지 않음)
#     - K: 카드뽑은 플레이어가 팔로워를 지정
# - 사탕획득의 전파
#     - 특정 플레이어가 사탕 획득할때 팔로워들도 연쇄적으로 사탕을 획득
#     - 팔로워의 팔로워도 획득
#     - 그러나 전파 과정 중 팔로워의 획득은 최대 1회까지로 제한됨


class Player:
    def __init__(self, idx_player):
        self.candy = 0
        self.follower = None
        self.left_player = None
        self.right_player = None
        self.idx_player = idx_player

    def __str__(self):
        return '<Player|idx=%d|candy=%d|follower=%d|left_player=%d|right_player=%d' % (
            self.idx_player,
            self.candy,
            self.follower.idx_player if self.follower is not None else -1,
            self.left_player.idx_player if self.left_player is not None else -1,
            self.right_player.idx_player if self.right_player is not None else -1
            )

    def set_follower(self, player):
        self.follower = player
    
    def add_candy(self, allow_propagation=True):
        self.candy += 1
        
        if allow_propagation:
            self.follower.add_candy()

    def add_candy_side(self):
        if self.right_player:
            self.right_player.add_candy()
        
        if self.left_player:
            self.left_player.add_candy()

    def assign_follower(self, follower):
        self.follower = follower


def main():
    num_player = int(input())
    
    # players init
    players = []
    for idx_player in range(num_player):
        players.append(Player(idx_player))
    
    # players on left and right setting
    if num_player > 1:
        for idx_player in range(num_player):
            if idx_player == 0:
                players[idx_player].left_player = players[num_player-1]
                players[idx_player].right_player = players[idx_player+1]
            elif idx_player == num_player-1:
                players[idx_player].left_player = players[idx_player-1]
                players[idx_player].right_player = players[0]
            else:
                players[idx_player].left_player = players[idx_player-1]
                players[idx_player].right_player = players[idx_player+1]

    # cards init
    cards = input().split()
    idx_player_now = 0

    # playing game
    iter_cards = iter(cards)
    while True:
        try:
            el = next(iter_cards)
        except StopIteration:
            break

        if el == 'K':
            follower = players[int(next(iter_cards))]
            players[idx_player_now].assign_follower(follower)
        # elif el == 'A':
        #     players[idx_player_now].add_candy()
        # elif el == 'J':
        #     players[idx_player_now].add_candy_side()
        elif el == 'Q':
            for player in players:
                player.add_candy(allow_propagation=False)

        idx_player_now += 1
        idx_player_now %= num_player

    # print out
    for player in players:
        print(player)

if __name__ == "__main__":
    main()