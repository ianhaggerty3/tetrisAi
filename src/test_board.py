import unittest

import numpy

import board
import piece


class TestPieceDrops(unittest.TestCase):
    test_board = board.Board()

    def tearDown(self):
        self.assertEqual(numpy.count_nonzero(self.test_board.board), 4)
        self.test_board.clear()

    def test_o_drop(self):
        test_piece = piece.Piece('O')
        self.test_board.drop_piece(0, test_piece)
        expected_array = numpy.array(([1, 1, 0, 0, 0, 0, 0, 0, 0, 0]), dtype=bool)
        numpy.testing.assert_array_equal(self.test_board.get_row(1), expected_array)
        numpy.testing.assert_array_equal(self.test_board.get_row(0), expected_array)

    def test_t_drop(self):
        test_piece = piece.Piece('T')
        self.test_board.drop_piece(0, test_piece)
        top_expected_array = numpy.array(([0, 1, 0, 0, 0, 0, 0, 0, 0, 0]), dtype=bool)
        bot_expected_array = numpy.array(([1, 1, 1, 0, 0, 0, 0, 0, 0, 0]), dtype=bool)
        numpy.testing.assert_array_equal(self.test_board.get_row(1), top_expected_array)
        numpy.testing.assert_array_equal(self.test_board.get_row(0), bot_expected_array)

    def test_l_drop(self):
        test_piece = piece.Piece('L')
        self.test_board.drop_piece(0, test_piece)
        top_expected_array = numpy.array(([0, 0, 1, 0, 0, 0, 0, 0, 0, 0]), dtype=bool)
        bot_expected_array = numpy.array(([1, 1, 1, 0, 0, 0, 0, 0, 0, 0]), dtype=bool)
        numpy.testing.assert_array_equal(self.test_board.get_row(1), top_expected_array)
        numpy.testing.assert_array_equal(self.test_board.get_row(0), bot_expected_array)

    def test_j_drop(self):
        test_piece = piece.Piece('J')
        self.test_board.drop_piece(0, test_piece)
        top_expected_array = numpy.array(([1, 0, 0, 0, 0, 0, 0, 0, 0, 0]), dtype=bool)
        bot_expected_array = numpy.array(([1, 1, 1, 0, 0, 0, 0, 0, 0, 0]), dtype=bool)
        numpy.testing.assert_array_equal(self.test_board.get_row(1), top_expected_array)
        numpy.testing.assert_array_equal(self.test_board.get_row(0), bot_expected_array)

    def test_s_drop(self):
        test_piece = piece.Piece('S')
        self.test_board.drop_piece(0, test_piece)
        top_expected_array = numpy.array(([0, 1, 1, 0, 0, 0, 0, 0, 0, 0]), dtype=bool)
        bot_expected_array = numpy.array(([1, 1, 0, 0, 0, 0, 0, 0, 0, 0]), dtype=bool)
        numpy.testing.assert_array_equal(self.test_board.get_row(1), top_expected_array)
        numpy.testing.assert_array_equal(self.test_board.get_row(0), bot_expected_array)

    def test_z_drop(self):
        test_piece = piece.Piece('Z')
        self.test_board.drop_piece(0, test_piece)
        top_expected_array = numpy.array(([1, 1, 0, 0, 0, 0, 0, 0, 0, 0]), dtype=bool)
        bot_expected_array = numpy.array(([0, 1, 1, 0, 0, 0, 0, 0, 0, 0]), dtype=bool)
        numpy.testing.assert_array_equal(self.test_board.get_row(1), top_expected_array)
        numpy.testing.assert_array_equal(self.test_board.get_row(0), bot_expected_array)

    def test_i_drop(self):
        test_piece = piece.Piece('I')
        self.test_board.drop_piece(0, test_piece)
        expected_array = numpy.array(([1, 0, 0, 0, 0, 0, 0, 0, 0, 0]), dtype=bool)
        numpy.testing.assert_array_equal(self.test_board.get_row(3), expected_array)
        numpy.testing.assert_array_equal(self.test_board.get_row(2), expected_array)
        numpy.testing.assert_array_equal(self.test_board.get_row(1), expected_array)
        numpy.testing.assert_array_equal(self.test_board.get_row(0), expected_array)


class TestGetHeight(unittest.TestCase):

    def test_get_height(self):
        test_board = board.Board()
        heights = test_board.get_heights()
        self.assertEqual(len(heights), 10)


if __name__ == '__main__':
    unittest.main()
