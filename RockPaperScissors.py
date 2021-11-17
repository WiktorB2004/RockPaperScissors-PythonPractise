import random

def play():
    user = input(
        "Whats your choice? 'r' for rock, 'p' for paper, 's' for scissors\n")
    computer = random.choice(['r', 'p', 's'])

    if user == computer:
        print("It's tie")
    if is_win(user, computer):
        print('You won!')
    print("You lost!")


def is_win(player, opponent):
    if (player == 'r' and opponent == 's') or (player == 's' and opponent == 'p') or (player == 'p' and opponent == 'r'):
        return True


play()
