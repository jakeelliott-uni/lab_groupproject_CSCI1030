class Piece:
    def __init__(self, row, col):
        self.row = row
        self.col = col

    def _valid_destination(self, row, col, blocked):
        return (
            0 <= row < 8
            and 0 <= col < 8
            and (row, col) != (self.row, self.col)
            and (row, col) not in blocked
        )

    def can_move(self, row, col, blocked):
        return False

    def path_clear(self, row, col, blocked):
        if not self._valid_destination(row, col, blocked):
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

    def move(self, row, col, blocked):
        if self.can_move(row, col, blocked):
            self.row = row
            self.col = col
            return True
        return False

class Bishop(Piece):
    def can_move(self, row, col, blocked):
        if not self.path_clear(row, col, blocked):
            return False
        if abs(row - self.row) != abs(col - self.col):
            return False

        return True

class King(Piece):
    def can_move(self, row, col, blocked):
        if not self._valid_destination(row, col, blocked):
            return False

        row_distance = abs(row - self.row)
        col_distance = abs(col - self.col)

        if row_distance > 1 or col_distance > 1:
            return False
       
        return True

class Knight(Piece):
    def can_move(self, row, col, blocked):
        if not self._valid_destination(row, col, blocked):
            return False
           
        diff_x = abs(row - self.row)
        diff_y = abs(col - self.col)

        if not ((diff_x == 1 and diff_y == 2) or (diff_y == 1 and diff_x == 2)):
            return False
       
        return True

class Pawn(Piece):
    def can_move(self, row, col, blocked):
        if not self.path_clear(row, col, blocked):
            return False

        row_diff = row - self.row
        col_diff = col - self.col

        if col_diff != 0 or row_diff > 1:
            return False

        return True

class Queen(Piece):
    def can_move(self, row, col, blocked):
        if not self.path_clear(row, col, blocked):
            return False
       
        is_straight = (row == self.row) or (col == self.col)
        is_diagonal = abs(row - self.row) == abs(col - self.col)
       
        if not (is_straight or is_diagonal):
            return False
       
        return True

class Rook(Piece):
    def can_move(self, row, col, blocked):
        if not self.path_clear(row, col, blocked):
            return False
        if row != self.row and col != self.col:
            return False
        return True