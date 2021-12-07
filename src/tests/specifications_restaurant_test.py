import unittest
from specifications.restaurant import *
import copy


class TestRestaurantSpecifications(unittest.TestCase):
    '''
    Tests all RestaurantSpecifications against a set of criteria.
    '''

    def setUp(self):
        self.lord_delicious = Restaurant(
            name='Lord Delicious',
            customer_rating=1,
            distance=7,
            average_price=35,
            cuisine='Russian'
        )
        self.palaceio = Restaurant(
            name='Palaceio',
            customer_rating=4,
            distance=7,
            average_price=45,
            cuisine='Malaysian'
        )
        self.spicy_palace = Restaurant(
            name='Spicy PalaceClick to check domain availability.',
            customer_rating=2,
            distance=6,
            average_price=10,
            cuisine='Vietnamese'
        )
        self.criteria_1 = RestaurantCriteria(
            restaurant_name='Lord',
            max_distance=10,
            max_price=3,
            min_customer_rating=2,
            cuisine='Vietnamese'
        )
        self.criteria_2 = RestaurantCriteria(
            restaurant_name='lord',
            max_distance=3,
            max_price=10,
            min_customer_rating=4,
            cuisine='Malaysian'
        )
        self.criteria_3 = RestaurantCriteria(
            restaurant_name='delic',
            max_distance=20,
            max_price=50,
            min_customer_rating=5,
            cuisine='vietnamese'
        )

    def test_restaurantIsTheRightName(self):
        criteria_1_copy = copy.deepcopy(self.criteria_1)
        criteria_1_copy.name = None

        # When name is None (not being filtered for), always return True
        self.assertTrue(RestaurantIsTheRightName(
        ).is_satisfied_by(self.lord_delicious, criteria_1_copy))

        criteria_1_copy.name = ''
        # When name is empty (not being filtered for), always return True
        self.assertTrue(RestaurantIsTheRightName(
        ).is_satisfied_by(self.lord_delicious, criteria_1_copy))

        self.assertTrue(RestaurantIsTheRightName(
        ).is_satisfied_by(self.lord_delicious, self.criteria_1))

        # Matches when lowercase
        self.assertTrue(RestaurantIsTheRightName(
        ).is_satisfied_by(self.lord_delicious, self.criteria_2))

        self.assertFalse(RestaurantIsTheRightName(
        ).is_satisfied_by(self.palaceio, self.criteria_1))

    def test_restaurantIsTheRightCuisine(self):
        criteria_1_copy = copy.deepcopy(self.criteria_1)
        criteria_1_copy.cuisine = None

        # When name is None (not being filtered for), always return True
        self.assertTrue(RestaurantIsTheRightCuisine(
        ).is_satisfied_by(self.lord_delicious, criteria_1_copy))

        criteria_1_copy.cuisine = ''
        # When name is empty (not being filtered for), always return True
        self.assertTrue(RestaurantIsTheRightCuisine(
        ).is_satisfied_by(self.lord_delicious, criteria_1_copy))

        self.assertFalse(RestaurantIsTheRightCuisine(
        ).is_satisfied_by(self.lord_delicious, self.criteria_1))

        self.assertTrue(RestaurantIsTheRightCuisine(
        ).is_satisfied_by(self.spicy_palace, self.criteria_1))

        # Matches when lowercase
        self.assertTrue(RestaurantIsTheRightCuisine(
        ).is_satisfied_by(self.spicy_palace, self.criteria_3))

    def test_restaurantIsCheapEnough(self):
        criteria_1_copy = copy.deepcopy(self.criteria_1)
        criteria_1_copy.max_price = None

        # When price is None (not being filtered for), always return True
        self.assertTrue(RestaurantIsCheapEnough(
        ).is_satisfied_by(self.lord_delicious, criteria_1_copy))

        self.assertTrue(RestaurantIsCheapEnough(
        ).is_satisfied_by(self.spicy_palace, self.criteria_3))

        self.assertFalse(RestaurantIsCheapEnough(
        ).is_satisfied_by(self.spicy_palace, self.criteria_1))

    def test_restaurantIsRatedWellEnough(self):
        criteria_1_copy = copy.deepcopy(self.criteria_1)
        criteria_1_copy.min_customer_rating = None

        # When min_customer_rating is None (not being filtered for), always return True
        self.assertTrue(RestaurantIsRatedWellEnough(
        ).is_satisfied_by(self.lord_delicious, criteria_1_copy))

        self.assertTrue(RestaurantIsRatedWellEnough(
        ).is_satisfied_by(self.spicy_palace, self.criteria_1))

        self.assertFalse(RestaurantIsRatedWellEnough(
        ).is_satisfied_by(self.spicy_palace, self.criteria_2))

    def test_restaurantIsCloseEnough(self):
        criteria_1_copy = copy.deepcopy(self.criteria_1)
        criteria_1_copy.max_distance = None

        # When max_distance is None (not being filtered for), always return True
        self.assertTrue(RestaurantIsCloseEnough(
        ).is_satisfied_by(self.lord_delicious, criteria_1_copy))

        self.assertTrue(RestaurantIsCloseEnough(
        ).is_satisfied_by(self.palaceio, self.criteria_1))

        self.assertFalse(RestaurantIsCloseEnough(
        ).is_satisfied_by(self.palaceio, self.criteria_2))


if __name__ == '__main__':
    unittest.main()
