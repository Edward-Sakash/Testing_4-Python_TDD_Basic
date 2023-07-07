import unittest
from app import rnd, max_num_in_list


class TestApp(unittest.TestCase):
    # check if max_num_in_list will return the right value
    def test_max_num_in_list1(self):
        self.assertEqual(
            max_num_in_list([2, 6, 8, 7, -1]),
            8,
            "Return value is not the greatest value in max_num_in_list",
        )

    # check if rnd returns the correct value
    def test_rnd1(self):
        start = 2
        end = 20
        result = rnd(start, end)

        # Check if the result is within the range [start, end]
        self.assertIn(result, range(2, 21))

    def test_rnd2(self):
        start = 2
        end = 20
        result = rnd(start, end)

        if result >= 21 or result < 2:
            self.fail("Out of range")
        else:
            pass


if __name__ == "__main__":
    unittest.main()
