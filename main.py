"""Loop to play connect4 in terminal"""
import connect4

def main():
    print("Let's play connect4!")
    game = connect4.Connect4()

    while not game.get_winner_id():
        col_played = game.ask_user_his_column()
        game.play_column(col_played)

    print(game.display_result())


if __name__ == "__main__":
    main()
