NB_COLUMNS = 6
NB_ROWS = 7

class Connect4:
    def __init__(self):
        self._board = [
            [0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0],
        ]

        self._board = []
        for row_num in range(NB_ROWS):
            row = []
            for col_num in range(NB_COLUMNS): 
                row.append(0)

            self._board.append(row)

        self._current_player = 1

    def ask_user_his_column(self):
        """Already implemented function to get the player's move in terminal"""
        print(self.display_board())
        col = input("In which column 1 (left) to 6 (right) do you put a coin?")
        return col

    def display_board(self):
        result = ""
        for row in self._board:
            result += "\n|"
            for cell in row:
                if cell == 0:
                    result += " "
                elif cell == 1:
                    result += "O"
                elif cell == 2:
                    result += "X"
            result += "|"

        return result + "\n"

    def play_column(self, col):
        last_row = 6
        while self._board[last_row][col-1] != 0:
            last_row = last_row - 1

        self._board[last_row][col - 1] = self._current_player
        self._current_player = 2 if self._current_player == 1 else 1

    def get_winner_id(self):
        for column_id in range(6):
            last_row = 6
            while (
                # Si le jeton ici est 0, il n'y a pas de jetons de joueur après
                self._board[last_row][column_id] != 0
                # Si la rangée est inférieure à 3, il ne reste que 3 rangée,
                # On ne peut plus faire 4 à la suite
                and last_row >= 3
            ):
                player_id = self._board[last_row][column_id]
                # Ce joueur a-t-il 4 jetons à la suite
                has_4_in_a_row =  all(
                    player_id == self._board[last_row - i][column_id]
                    for i in range(4)
                )
                if has_4_in_a_row:
                    return player_id
                else:
                    last_row -= 1

        return 0


