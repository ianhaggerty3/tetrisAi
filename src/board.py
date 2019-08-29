from typing import List

import numpy

import helper as h
import piece as p

helper = h.Helper()


class Board:
    def __init__(self):
        self.height = 40
        self.width = 10
        self.board = numpy.zeros((self.height, self.width), dtype=bool)

    def clear(self) -> None:
        self.board = numpy.zeros((self.height, self.width), dtype=bool)

    # Returns a copy of the row
    def get_row(self, row_num: int) -> numpy.ndarray:
        return self.board[self.height - row_num - 1]

    # Returns a copy of the column
    def get_col(self, col_num: int) -> numpy.ndarray:
        return [x[col_num] for x in self.board]

    def set_row(self, row: numpy.ndarray, row_num: int) -> None:
        self.board[self.height - row_num] = row

    def set_col(self, col: numpy.ndarray, col_num: int) -> None:
        self.board[:][col_num] = col

    def copy_piece(self, piece: p.Piece, x: int, y: int) -> None:
        adjusted_y = self.height - (y + piece.height)
        self.board[adjusted_y:adjusted_y+piece.height, x:x+piece.width] = piece.piece

    def drop_piece(self, col_num: int, piece: p.Piece) -> None:
        board_heights = self.get_heights()
        y_coord = helper.get_max_over_range(board_heights, col_num, col_num + piece.width)

        # This method for dropping pieces does not allow t-spins; it is a hard-drop only system
        self.copy_piece(piece, col_num, y_coord)

    def get_heights(self) -> List[int]:
        heights = []
        for x in range(self.width):
            y = 0
            while y < self.height:
                if self.board[y][x]:
                    heights.append(self.height - y)
                    y = self.height + 1
                elif y == self.height - 1:
                    heights.append(0)
                y += 1

        return heights
