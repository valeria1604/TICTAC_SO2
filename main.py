from studentA import print_board, is_game_over, new_board_3, new_board_5
from studentB import ai_move, get_user_move, is_player_starting
from studentA import announce_outcome

if __name__ == '__main__':
    choice_size = input("Jaki rozmiar planszy chcesz?(3/5): ")
    if choice_size == '3':
        board = new_board_3(size=3)
        players_move = is_player_starting()
        while not is_game_over(board):
            print_board(board)
            if players_move:
                board = get_user_move(board)
            else:
                board = ai_move(board)
            players_move = not players_move
        print_board(board)
        announce_outcome(board, players_move)

    elif choice_size == '5':
        board = new_board_5(size=5)
        players_move = is_player_starting()
        while not is_game_over(board):
            print_board(board)
            if players_move:
                board = get_user_move(board)
            else:
                board = ai_move(board)
            players_move = not players_move
        print_board(board)
        announce_outcome(board, players_move)
    else:
        print("Odpowiedz niewlasciwa.")




