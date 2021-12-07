import unittest
from specifications.restaurant import *
from index import make_parser


class TestCommandLineInputValidity(unittest.TestCase):
    '''
    Tests the validity of function input from the command line.
    '''

    def setUp(self):
        self.parser = make_parser()

    def test_price(self):
        with self.assertRaises(SystemExit):
            self.parser.parse_args(['--price', '-1'])
        with self.assertRaises(SystemExit):
            self.parser.parse_args(['--price', 'hello'])
        self.assertEqual(self.parser.parse_args(['-p', '10']).price, 10.0)
        self.assertEqual(self.parser.parse_args(['-p', '11']).price, 11.0)

        # defaults to None
        self.assertEqual(self.parser.parse_args([]).price, None)

    def test_distance(self):
        with self.assertRaises(SystemExit):
            self.parser.parse_args(['--distance', '-12'])
        self.assertEqual(self.parser.parse_args(['-d', '0.76']).distance, 0.76)
        self.assertEqual(self.parser.parse_args(['-d', '14']).distance, 14)

        # defaults to None
        self.assertEqual(self.parser.parse_args([]).distance, None)

    def test_customer_rating(self):
        with self.assertRaises(SystemExit):
            self.parser.parse_args(['--customer-rating', '-12'])
        with self.assertRaises(SystemExit):
            self.parser.parse_args(['--customer-rating', '6'])
        with self.assertRaises(SystemExit):
            self.parser.parse_args(['--customer-rating', '3.76'])

        self.assertEqual(self.parser.parse_args(
            ['--customer-rating', '3']).customer_rating, 3)
        self.assertEqual(self.parser.parse_args(
            ['--customer-rating', '1']).customer_rating, 1)

        # defaults to None
        self.assertEqual(self.parser.parse_args([]).customer_rating, None)

    def test_files(self):

        # Must be a CSV
        with self.assertRaises(SystemExit):
            self.parser.parse_args(['--restaurant-file', 'restaurants.py'])

        # Must exist in the csv/ folder
        with self.assertRaises(SystemExit):
            self.parser.parse_args(['--f', 'hello'])
        with self.assertRaises(SystemExit):
            self.parser.parse_args(['--cuisine-file', 'cuisines.py'])

        self.assertEqual(self.parser.parse_args(
            ['-f', 'cuisines.csv']).cuisine_file, 'cuisines.csv')
        self.assertEqual(self.parser.parse_args(
            ['-f', 'restaurants.csv']).restaurant_file, 'restaurants.csv')

        # Defaults to valid CSVs
        self.assertEqual(self.parser.parse_args([]
                                                ).restaurant_file, 'restaurants.csv')
        self.assertEqual(self.parser.parse_args([]
                                                ).cuisine_file, 'cuisines.csv')

    def test_names(self):
        self.assertEqual(self.parser.parse_args(
            ['--name', 'McDonald\'s']).name, 'McDonald\'s')
        self.assertEqual(self.parser.parse_args(
            ['-n', '12345']).name, '12345')
        self.assertEqual(self.parser.parse_args(
            ['--cuisine', 'Chi']).cuisine, 'Chi')
        self.assertEqual(self.parser.parse_args(
            ['-c', '12345']).cuisine, '12345')

        # defaults to None
        self.assertEqual(self.parser.parse_args([]).name, None)

    def test_name(self):
        self.assertEqual(self.parser.parse_args(
            ['--name', 'McDonald\'s']).name, 'McDonald\'s')
        self.assertEqual(self.parser.parse_args(
            ['-n', '12345']).name, '12345')

        # defaults to None
        self.assertEqual(self.parser.parse_args([]).name, None)


if __name__ == '__main__':
    unittest.main()
