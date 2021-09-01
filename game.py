import random


victory = 0
tie = 0
lost = 0


def user_win(player, opponent):
    if (player == 'К' and opponent == 'Н') or (player == 'Н' and opponent == 'Б') \
            or (player == 'Б' and opponent == 'К'):
        return True


def play():
    global victory
    global tie
    global lost
    user = input("'К' - камень, 'Н' - ножницы, 'Б' - бумага\n").upper()
    computer = random.choice(['К', 'Н', 'Б'])
    print(f'Компьютер выкидывает: {computer.upper()}')
    if user_win(user, computer):
        victory += 1
        print(f'Побед: {victory}, Ничьих: {tie}, Поражений: {lost}')
        return print('Славная Победа!\n')
    if user == computer:
        tie += 1
        print(f'Побед: {victory}, Ничьих: {tie}, Поражений: {lost}')
        return print('Ничья\n')
    else:
        lost += 1
        print(f'Побед: {victory}, Ничьих: {tie}, Поражений: {lost}')
        return print('Поражение!\n')


if __name__ == '__main__':
    while True:
        play()
