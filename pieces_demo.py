class Piece:
    def __init__(self, row, col):
        self.row = row
        self.col = col

    # Destination must be on the board, not the current square, and either empty or an enemy piece.
    def _valid_destination(self, row, col, blocked, enemies=()):
        return (
            0 <= row < 8
            and 0 <= col < 8
            and (row, col) != (self.row, self.col)
            and ((row, col) not in blocked or (row, col) in enemies)
        )

    # To be inherited
    def can_move(self, row, col, blocked, enemies=()):
        return False

    # Checks that every square BETWEEN the piece and the destination is empty.
    def path_clear(self, row, col, blocked, enemies=()):
        if not self._valid_destination(row, col, blocked, enemies):
            return False

        # Only straight lines and diagonals have a "path" (this prevents the infinite loop)
        row_dist = abs(row - self.row)
        col_dist = abs(col - self.col)
        if not (row_dist == 0 or col_dist == 0 or row_dist == col_dist):
            return False

        row_step = self.direction_step(self.row, row)
        col_step = self.direction_step(self.col, col)

        current_row = self.row + row_step
        current_col = self.col + col_step

        while (current_row, current_col) != (row, col):
            if (current_row, current_col) in blocked:
                return False
            current_row += row_step
            current_col += col_step

        return True

    def direction_step(self, start, end):
        if start < end:
            return 1
        if start > end:
            return -1
        return 0

    # The method that is called by the GUI
    def move(self, row, col, blocked, enemies=()):
        if self.can_move(row, col, blocked, enemies):
            self.row = row
            self.col = col
            return True
        return False


class Bishop(Piece):
    def can_move(self, row, col, blocked, enemies=()):
        if abs(row - self.row) != abs(col - self.col):
            return False
        return self.path_clear(row, col, blocked, enemies)


class King(Piece):
    def can_move(self, row, col, blocked, enemies=()):
        if not self._valid_destination(row, col, blocked, enemies):
            return False
        return abs(row - self.row) <= 1 and abs(col - self.col) <= 1


class Knight(Piece):
    def can_move(self, row, col, blocked, enemies=()):
        if not self._valid_destination(row, col, blocked, enemies):
            return False
        diff_x = abs(row - self.row)
        diff_y = abs(col - self.col)
        return (diff_x == 1 and diff_y == 2) or (diff_x == 2 and diff_y == 1)


class Pawn(Piece):
    # color is "white" or "black". Assumes white starts at the bottom (rows 6-7)
    # and moves toward row 0. Flip the direction if your board is the other way.
    def __init__(self, row, col, color="white"):
        super().__init__(row, col)
        self.color = color
        self.direction = -1 if color == "white" else 1
        self.start_row = row

    def can_move(self, row, col, blocked, enemies=()):
        if not self._valid_destination(row, col, blocked, enemies):
            return False

        forward = (row - self.row) * self.direction   # 1 = one step forward
        sideways = abs(col - self.col)

        # Diagonal capture: only if an enemy is there
        if forward == 1 and sideways == 1:
            return (row, col) in enemies

        # Straight moves: destination must be empty (pawns can't capture forward)
        if sideways == 0 and (row, col) not in blocked:
            if forward == 1:
                return True
            if forward == 2 and self.row == self.start_row:
                square_between = (self.row + self.direction, self.col)
                return square_between not in blocked

        return False


class Queen(Piece):
    def can_move(self, row, col, blocked, enemies=()):
        is_straight = (row == self.row) or (col == self.col)
        is_diagonal = abs(row - self.row) == abs(col - self.col)
        if not (is_straight or is_diagonal):
            return False
        return self.path_clear(row, col, blocked, enemies)


class Rook(Piece):
    def can_move(self, row, col, blocked, enemies=()):
        if row != self.row and col != self.col:
            return False
        return self.path_clear(row, col, blocked, enemies)
