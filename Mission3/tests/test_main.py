import unittest


class TestTaskManager(unittest.TestCase):

    def test_addition(self):

        self.assertEqual(2 + 2, 4)

    def test_uppercase(self):

        self.assertEqual("python".upper(), "PYTHON")


if __name__ == "__main__":

    unittest.main()