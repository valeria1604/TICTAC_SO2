import random
import time

def is_player_starting():
    #pobieranie i uzywanie decyzji uzytkownika
    choice = input("Czy ty chcesz zaczac? (yes/no): ").strip().lower()
    if choice == 'yes':
        return True
    elif choice == 'no':
        return False
    else:
        print("Odpowiedz niewlasciwa.")
        return random.choice([True, False])

def get_user_move(board):
    size = len(board)
    start_time = time.time()
    while True:
        try:
            #uzytkownik ma tylko 5 sekund na decyzje
            if time.time() - start_time > 5:
                print("Czas skonczyl sie.")
                return board
            move = input("Napisz swoj krok w postaci [row,col]: ")
            row, col = map(int, move.split(','))
            if board[row][col] == ' ':
                board[row][col] = 'X'
                return board
            else:
                print("Miejsce juz jest zajete.")
        except ValueError:
            print("Niewlasciwa postac.")

def ai_move(board):
    #generowanie ruchu komputera
    size = len(board)
    for i in range(size):
        for j in range(size):
            if board[i][j] == ' ':
                board[i][j] = 'O'
                return board
    return board

