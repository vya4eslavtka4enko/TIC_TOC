from IPython.display import clear_output

board = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ]
game_over = False


def check_win():
    global game_over
    if board[1] == "X" and board[2] == "X" and board[3] == "X" or board[1] == "O" and board[2] == "O" and board[
        3] == "O":
        game_over = True
    elif board[4] == "X" and board[5] == "X" and board[6] == "X" or board[4] == "O" and board[5] == "O" and board[
        6] == "O":
        game_over = True
    elif board[7] == "X" and board[8] == "X" and board[9] == "X" or board[7] == "O" and board[8] == "O" and board[
        9] == "O":
        game_over = True
    elif board[3] == "X" and board[5] == "X" and board[7] == "X" or board[3] == "O" and board[5] == "O" and board[
        7] == "O":
        game_over = True
    elif board[9] == "X" and board[5] == "X" and board[1] == "X" or board[9] == "O" and board[5] == "O" and board[
        1] == "O":
        game_over = True
    elif board[3] == "X" and board[6] == "X" and board[9] == "X" or board[3] == "O" and board[6] == "O" and board[
        9] == "O":
        game_over = True
    elif board[2] == "X" and board[5] == "X" and board[8] == "X" or board[2] == "O" and board[5] == "O" and board[
        8] == "O":
        game_over = True
    elif board[1] == "X" and board[4] == "X" and board[7] == "X" or board[1] == "O" and board[4] == "O" and board[
        7] == "O":
        game_over = True


def choose_marker():
    marker_player_first = ''
    marker_player_second = ''
    marker = ''
    while marker != 'x' and marker != 'o':
        marker = input('Player 1 choose your marker [ x or o ] ')
        if marker == 'x':
            print('First player choose X')
            print("Second player play O")
            marker_player_first = 'X'
            marker_player_second = 'O'
        elif marker == 'o':
            print('First player choose O')
            print("Second player play X")
            marker_player_first = 'O'
            marker_player_second = 'X'
        else:
            print('Make a selection')
    return marker_player_second, marker_player_first


def render_dashboard():
    clear_output()
    print('|' + board[1] + '|' + board[2] + '|' + board[3] + '|')
    print('-' + " " + '-' + " " + '-' + " " + '-')
    print('|' + board[4] + '|' + board[5] + '|' + board[6] + '|')
    print('-' + " " + '-' + " " + '-' + " " + '-')
    print('|' + board[7] + '|' + board[8] + '|' + board[9] + '|')


def game():
    global game_over
    choice_m = choose_marker()
    while not game_over:
        check_win()
        try:
            choiсe_number = int(input("Make your choice Player 1 "))
        except:
            print('Yor are not enter correct number ')
        board[choiсe_number] = choice_m[1]
        render_dashboard()
        try:
            choiсe_number = int(input("Make your choice Player 2 "))
        except:
            print('Yor are not enter correct number ')
        board[choiсe_number] = choice_m[0]
        render_dashboard()



game()
