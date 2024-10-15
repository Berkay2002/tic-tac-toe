class TicTacToe:
    def __init__(self):
        self.board = [[' ' for _ in range(3)] for _ in range(3)]
        self.current_player = 'X'
        self.winner = None

    def print_board(self):
        print("\n  0 1 2")
        for idx, row in enumerate(self.board):
            print(f"{idx} {' '.join(row)}")

    def make_move(self, row, col):
        if self.board[row][col] == ' ':
            self.board[row][col] = self.current_player
            if self.check_winner(row, col):
                self.winner = self.current_player
            else:
                self.current_player = 'O' if self.current_player == 'X' else 'X'
            return True
        return False

    def check_winner(self, row, col):
        # Kontrollera rad
        if all(self.board[row][c] == self.current_player for c in range(3)):
            return True
        # Kontrollera kolumn
        if all(self.board[r][col] == self.current_player for r in range(3)):
            return True
        # Kontrollera diagonaler
        if row == col and all(self.board[i][i] == self.current_player for i in range(3)):
            return True
        if row + col == 2 and all(self.board[i][2 - i] == self.current_player for i in range(3)):
            return True
        return False

    def is_game_over(self):
        if self.winner or all(cell != ' ' for row in self.board for cell in row):
            return True
        return False
