import random

# Функция для отображения игровой доски
def display_board(board):
    print(board[1] + '|' + board[2] + '|' + board[3])
    print('-+-+-')
    print(board[4] + '|' + board[5] + '|' + board[6])
    print('-+-+-')
    print(board[7] + '|' + board[8] + '|' + board[9])

# Функция для выбора места хода игрока
def player_input():
    marker = ''
    while not (marker == 'X' or marker == 'O'):
        marker = input('Выберите Х или О для игры: ').upper()
    if marker == 'X':
        return ('X', 'O')
    else:
        return ('O', 'X')

# Функция для установки маркера на доске
def place_marker(board, marker, position):
    board[position] = marker

# Функция для проверки выигрышной комбинации
def win_check(board, mark):
    return ((board[1] == board[2] == board[3] == mark) or
            (board[4] == board[5] == board[6] == mark) or
            (board[7] == board[8] == board[9] == mark) or
            (board[1] == board[4] == board[7] == mark) or
            (board[2] == board[5] == board[8] == mark) or
            (board[3] == board[6] == board[9] == mark) or
            (board[1] == board[5] == board[9] == mark) or
            (board[3] == board[5] == board[7] == mark))

# Функция для выбора хода бота
def choose_first():
    if random.randint(0, 1) == 0:
        return 'Бот'
    else:
        return 'Игрок'

# Функция для проверки доступности места для хода
def space_check(board, position):
    return board[position] == ' '

# Функция для проверки заполненности доски
def full_board_check(board):
    for i in range(1, 10):
        if space_check(board, i):
            return False
    return True

# Функция для выбора хода игрока
def player_choice(board):
    position = 0
    while position not in range(1, 10) or not space_check(board, position):
        position = int(input('Выберите следующий ход (1-9): '))
    return position

# Функция для хода бота
def bot_choice(board):
    available_positions = [i for i in range(1, 10) if space_check(board, i)]
    return random.choice(available_positions)

# Функция для повторной игры
def replay():
    return input('Хотите сыграть еще? Введите "да" или "нет": ').lower().startswith('д')

# Основной игровой цикл
print('Добро пожаловать в игру крестики-нолики!')

while True:
    the_board = [' '] * 10
    player_marker, bot_marker = player_input()
    turn = choose_first()
    print(turn + ' ходит первым.')
    game_on = True

    while game_on:
        if turn == 'Игрок':
            display_board(the_board)
            position = player_choice(the_board)
            place_marker(the_board, player_marker, position)

            if win_check(the_board, player_marker):
                display_board(the_board)
                print('Поздравляю! Вы выиграли!')
                game_on = False
            else:
                if full_board_check(the_board):
                    display_board(the_board)
                    print('Ничья!')
                    break
                else:
                    turn = 'Бот'
        else:
            position = bot_choice(the_board)
            place_marker(the_board, bot_marker, position)

            if win_check(the_board, bot_marker):
                display_board(the_board)
                print('Бот победил! Вы проиграли.')
                game_on = False
            else:
                if full_board_check(the_board):
                    display_board(the_board)
                    print('Ничья!')
                    break
                else:
                    turn = 'Игрок'

    if not replay():
        break