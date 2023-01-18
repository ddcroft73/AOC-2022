import os

fpath: str = os.getcwd() + '/input.txt'


# simple translation part one
def decode_simple(text: str) -> tuple[str]:
    opponent_decode = {'A': 'rock', 'B': 'paper', 'C': 'scissors'}
    player_decode = {'X': 'rock', 'Y': 'paper', 'Z': 'scissors'}
    op_throw: str = text[0]
    my_throw: str = text[2]
    return opponent_decode[op_throw], player_decode[my_throw]

# Decides what the player needs to throw to carry out the strategy, based on the data in input.txt
def decode_strategy(text: str) -> tuple[str]:    
    input_a: str = text[0]
    input_b: str = text[2]
    opponent_decode = {'A': 'rock', 'B': 'paper', 'C': 'scissors'}
    str_to_num = {'rock': 1, 'paper': 2, 'scissors': 3} 
    num_to_str = {1: 'rock', 2: 'paper', 3: 'scissors'}    
   
    op_throw_str: str = opponent_decode[input_a]  # ops play translated to r, p or s
    op_throw_num = str_to_num[op_throw_str]       # the number value of their play.
    elven_strategy: str = input_b                 # startegy from input file
    my_throw_num: str = None                      # This will be the key used in num_to_str to 
                                                  # select the throw as per the strategy guide
     
    if (elven_strategy == 'X'):  # lose
        my_throw_num = op_throw_num - 1

    if (elven_strategy == 'Y'):  # draw
        my_throw_num = op_throw_num

    if (elven_strategy == 'Z'):  # win the round.
        my_throw_num = op_throw_num + 1

    if (my_throw_num > 3):
        my_throw_num = 1
    if (my_throw_num < 1):
        my_throw_num = 3

    #my_strat = {'X': 'Lose', 'Y': 'Draw', 'Z': "Win"}
    #print('----------------------------------------------------------')
    #print(f'Op played: {op_throw_str}')
    #print(f'My strategy says I need to: {my_strat[elven_strategy]}')
    #print(f'Therefore, my Choioce  is: { num_to_str[my_throw_num]}')

    return opponent_decode[input_a], num_to_str[my_throw_num]


def get_winner(op_throw: str, pl_throw: str) -> tuple[str]:
    def score_weapon(weapon: str) -> int:
        res: int = 0
        if (weapon == 'rock'):
            res = 1
        elif (weapon == 'paper'):
            res = 2
        elif (weapon == 'scissors'):
            res = 3
        return res

    round: int = 0  # default to player loss
    weapon: int = 0
    winner: str = 'Opponent'

    player_wins_profiles: list[str] = [
        "rock scissors",
        "scissors paper",
        "paper rock"
    ]

    match_result: str = pl_throw + ' ' + op_throw

    for profile in player_wins_profiles:
        if (op_throw == pl_throw):
            round = 3  # tie
            winner = 'Draw'
            break

        if (profile == match_result):
            round = 6  # player won
            winner = 'Player'
            break

    weapon = score_weapon(pl_throw)

    return ( 
        round, weapon, winner
    )



def part_one():
    total_score: int = 0
    weapon_score: int = 0
    round_score: int = 0
    winner: str = None

    with open(fpath, 'r') as file:
            games: list[str] = file.readlines()

            for line_cnt, match in enumerate(games):
                opponent_throw, player_throw = decode_simple(match)
                round_score, weapon_score, winner = get_winner(opponent_throw, player_throw)
                total_score += (round_score + weapon_score)

            #    print( f'\nMatch: {line_cnt} Part One\n------------------------------------------------------------')
            #    print(f'Player: {player_throw.upper()} Opponent: {opponent_throw.upper()}')
            #    print(f'Score this round: {round_score}, Weapon Score: {weapon_score} \nTotal: {total_score}')
            #    print(f'Winner is: {winner[0]}')

    print(f'Part One total score: {total_score}')

def part_two():
    
    total_score: int = 0
    weapon_score: int = 0
    round_score: int = 0
    winner: str = None
    
    with open(fpath, 'r') as file:
        games: list[str] = file.readlines()

        for line_cnt, match in enumerate(games):
            opponent_throw, player_throw = decode_strategy(match)
            round_score, weapon_score, winner = get_winner(opponent_throw, player_throw)
            total_score += (round_score + weapon_score)

           # print( f'\nMatch: {line_cnt} Part Two\n------------------------------------------------------------')
           # print(f'Opponent: {opponent_throw.upper()} Player: {player_throw.upper()}')
           # print(f'Score this round: {round_score}, Weapon Score: {weapon_score} \nTotal: {total_score}\n')
           # print(f'Winner is: {winner[0]}')

    print(f'Part Two total score: {total_score}')


def main() -> None:
    part_one()
    part_two()     


if __name__ == "__main__":
    main()

