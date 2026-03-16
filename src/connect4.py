NB_COLUMNS = 6
NB_ROWS = 7

class Connect4:
    def ask_user_his_column(self):
        """Already implemented function to get the player's move in terminal"""
        print(self.display_board())
        col = input("In which column 1 (left) to 6 (right) do you put a coin?")
        return col

    def display_board(self):
        return "wrong board"
