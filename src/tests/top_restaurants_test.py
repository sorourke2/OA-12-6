import unittest
from index import RestaurantCriteria
from search_restaurants_program import Restaurant
from search_restaurants_program import FilterRestaurantsCSVProgram


class TestFindingTopRestraunts(unittest.TestCase):
    '''
    Tests the passing in of criteria into the program and the outputting of
    the top restaurants based on the given criteria.
    '''

    def setUp(self):
        self.program = FilterRestaurantsCSVProgram(
            'cuisines.csv', 'boston_restaurants.csv')

    def test_single_name_criteria(self):
        criteria = RestaurantCriteria(
            restaurant_name='grill',
            max_distance=None,
            max_price=None,
            min_customer_rating=None,
            cuisine=None
        )
        sorted_results = [Restaurant(
            name='George\'s Grill',
            customer_rating=4,
            distance=7,
            average_price=20,
            cuisine='Vietnamese'
        ), Restaurant(
            name='Grill Up',
            customer_rating=3,
            distance=7,
            average_price=50,
            cuisine='American'
        )]
        self.assertEqual(self.program.get_top_restaurants(
            criteria), sorted_results)

    def test_no_criteria(self):
        # Overall tests how sorting acts
        criteria = RestaurantCriteria(
            restaurant_name=None,
            max_distance=None,
            max_price=None,
            min_customer_rating=None,
            cuisine=None
        )

        '''
        Sorts distance first
         - Therefore Happy's at the top
        Then Customer rating
          - Therefore Omalio's and George's grill are next
        Then Price
          - grill Up and Sweet Happy same rating, distance, and price. Therefore
          the order is "random"/just the default ordering.
        '''
        sorted_results = [
            Restaurant(
                name='Happy\'s',
                customer_rating=4,
                distance=1,
                average_price=10,
                cuisine='Spanish'
            ), Restaurant(
                name='Omalio\'s',
                customer_rating=4,
                distance=6,
                average_price=50,
                cuisine='American'
            ), Restaurant(
                name='George\'s Grill',
                customer_rating=4,
                distance=7,
                average_price=20,
                cuisine='Vietnamese'
            ), Restaurant(
                name='Grill Up',
                customer_rating=3,
                distance=7,
                average_price=50,
                cuisine='American'
            ), Restaurant(
                name='Sweet Happy',
                customer_rating=3,
                distance=7,
                average_price=50,
                cuisine='American'
            )
        ]
        self.assertEqual(self.program.get_top_restaurants(
            criteria), sorted_results)


if __name__ == '__main__':
    unittest.main()
