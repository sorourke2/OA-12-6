import unittest
from index import RestaurantCriteria
from search_restaurants_program import Restaurant
from search_restaurants_program import FilterRestaurantsCSVProgram


class TestRestaurantValidity(unittest.TestCase):
    '''
    Tests the checking of validity of Restaurants based on some given
    criteria.
    '''

    def setUp(self):
        self.program = FilterRestaurantsCSVProgram('', '')
        self.rest_1 = Restaurant(
            name='Lord Delicious',
            customer_rating=1,
            distance=7,
            average_price=35,
            cuisine='Russian'
        )
        self.rest_2 = Restaurant(
            name='Hilltop Delicious',
            customer_rating=3,
            distance=3,
            average_price=45,
            cuisine='Japanese'
        )
        self.buggy_restaurant_name = Restaurant(
            name='Spicy PalaceClick to check domain availability.',
            customer_rating=2,
            distance=6,
            average_price=10,
            cuisine='Vietnamese'
        )
        self.by_name_only = RestaurantCriteria(
            restaurant_name='Lord',
            max_distance=None,
            max_price=None,
            min_customer_rating=None,
            cuisine=None
        )
        self.name_and_distance = RestaurantCriteria(
            restaurant_name='delic',
            max_distance=10,
            max_price=None,
            min_customer_rating=None,
            cuisine=None
        )
        self.name_and_cuisine = RestaurantCriteria(
            restaurant_name='delic',
            max_distance=None,
            max_price=None,
            min_customer_rating=None,
            cuisine='ja'
        )
        self.all_criteria = RestaurantCriteria(
            restaurant_name='check',
            max_distance=9,
            max_price=14,
            min_customer_rating=1,
            cuisine='viet'
        )

    def test_solo_name(self):
        self.assertTrue(self.program._is_valid_restaurant(
            self.rest_1, self.by_name_only))

    def test_name_and_distance(self):
        self.assertTrue(self.program._is_valid_restaurant(
            self.rest_1, self.name_and_distance))
        self.assertTrue(self.program._is_valid_restaurant(
            self.rest_2, self.name_and_distance))
        self.assertFalse(self.program._is_valid_restaurant(
            self.buggy_restaurant_name, self.name_and_distance))

    def test_name_and_cuisine(self):
        self.assertFalse(self.program._is_valid_restaurant(
            self.rest_1, self.name_and_cuisine))
        self.assertTrue(self.program._is_valid_restaurant(
            self.rest_2, self.name_and_cuisine))

    def test_all_criteria_match(self):
        self.assertTrue(self.program._is_valid_restaurant(
            self.buggy_restaurant_name, self.all_criteria))
        self.assertFalse(self.program._is_valid_restaurant(
            self.rest_2, self.all_criteria))


if __name__ == '__main__':
    unittest.main()
