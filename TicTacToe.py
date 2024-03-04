
class TicTacToe:
    def __init__(self):
        self.board = [" " for _ in range(9)]  # Initialize an empty 3x3 board
        self.current_player = "X"  # Start with player X
        self.winner = None

    def display_board(self):
        """Display the current state of the board."""
        print("\n")
        for row in [self.board[i:i + 3] for i in range(0, 9, 3)]:
            print(" | ".join(row))
            print("-" * 9)

    def make_move(self, position):
        """Make a move on the board."""
        if self.board[position] == " ":
            self.board[position] = self.current_player
            self.check_winner()
            self.current_player = "O" if self.current_player == "X" else "X"
        else:
            print("Invalid move. Try again.")

    def check_winner(self):
        """Check if there's a winner."""
        winning_combinations = [
            (0, 1, 2), (3, 4, 5), (6, 7, 8),  # Rows
            (0, 3, 6), (1, 4, 7), (2, 5, 8),  # Columns
            (0, 4, 8), (2, 4, 6)  # Diagonals
        ]
        for combo in winning_combinations:
            a, b, c = combo
            if self.board[a] == self.board[b] == self.board[c] != " ":
                self.winner = self.board[a]
                break

    def play_game(self):
        """Main game loop."""
        while not self.winner and " " in self.board:
            self.display_board()
            try:
                position = int(input(f"{self.current_player}'s turn. Enter position (0-8): "))
                self.make_move(position)
            except ValueError:
                print("Invalid input. Please enter a number between 0 and 8.")

        self.display_board()
        if self.winner:
            print(f"{self.winner} wins!")
        else:
            print("It's a tie!")

if __name__ == "__main__":
    game = TicTacToe()
    game.play_game()
