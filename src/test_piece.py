import unittest

import numpy

import piece


class TestDefaultPieces(unittest.TestCase):
    piece_types = piece.PieceTypes()

    def test_block_size(self):
        for name, test_block in self.piece_types.pieceLookup.items():
            self.assertEqual(numpy.count_nonzero(test_block), 4)


if __name__ == '__main__':
    unittest.main()
