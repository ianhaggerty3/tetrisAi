import unittest

import helper as h

helper = h.Helper()


class TestGetMaxOverRange(unittest.TestCase):

    def test_normal_range(self):
        test_array = list(range(4))
        self.assertEqual(helper.get_max_over_range(test_array, 0, len(test_array)), 3)

    def test_restrictive_range(self):
        test_array = list(range(5))
        self.assertEqual(helper.get_max_over_range(test_array, 0, len(test_array) - 1), 3)


class TestGetDiffs(unittest.TestCase):

    def test_normal_array(self):
        test_array = list(range(3))
        expected_array = [(0, -1), (1, -1), (1, 0)]
        self.assertEqual(helper.get_diffs(test_array), expected_array)


if __name__ == '__main__':
    unittest.main()
