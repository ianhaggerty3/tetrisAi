import numpy


class PieceTypes:
    def __init__(self):
        # Default piece orientations
        self.OPiece = numpy.array(([1, 1], [1, 1]), dtype=bool)
        self.TPiece = numpy.array(([0, 1, 0], [1, 1, 1]), dtype=bool)
        self.LPiece = numpy.array(([0, 0, 1], [1, 1, 1]), dtype=bool)
        self.JPiece = numpy.array(([1, 0, 0], [1, 1, 1]), dtype=bool)
        self.SPiece = numpy.array(([0, 1, 1], [1, 1, 0]), dtype=bool)
        self.ZPiece = numpy.array(([1, 1, 0], [0, 1, 1]), dtype=bool)
        self.IPiece = numpy.array(([1], [1], [1], [1]), dtype=bool)
        self.pieceLookup = {
             'O': self.OPiece,
             'T': self.TPiece,
             'L': self.LPiece,
             'J': self.JPiece,
             'S': self.SPiece,
             'Z': self.ZPiece,
             'I': self.IPiece,
             }

    def get_piece(self, piece: str) -> numpy.ndarray:
        return self.pieceLookup[piece.upper()]


class Piece:
    def __init__(self, piece_type: str):
        self.piece_type = piece_type
        self.piece_types = PieceTypes()
        self.piece = self.piece_types.get_piece(piece_type)
        self.height = len(self.piece)
        self.width = len(self.piece[0])

    # Returns a copy of the row
    def get_row(self, row_num: int) -> numpy.ndarray:
        return self.board[self.height - row_num]

    # Returns a copy of the column
    def get_col(self, col_num: int) -> numpy.ndarray:
        return [x[col_num] for x in self.board]

    def rotate_counterclockwise(self) -> None:
        numpy.rot90(self.piece, 1)

    def rotate_clockwise(self) -> None:
        numpy.rot90(self.piece, 3)
