from typing import List, Dict, Set
import csv
from specifications.restaurant import RestaurantIsTheRightName, RestaurantIsCheapEnough, RestaurantIsCloseEnough, RestaurantIsRatedWellEnough, RestaurantIsTheRightCuisine, RestaurantIsTheRightName
from models.restaurant import Restaurant
from models.restaurant_criteria import RestaurantCriteria


class FilterRestaurantsCSVProgram(object):
    '''
    Program which takes in two csv files with cuisine info and restaurant info.
    Provides the functionality of parsing these csv files into objects only if
    they match a given set of RestaurantCriteria. Provides the ability to sort
    these matches as well as tabulate the results on the command line.
    '''

    def __init__(self, cuisine_file_name: str, restaurant_file_name: str):
        self.cuisine_file_name = cuisine_file_name
        self.restaurant_file_name = restaurant_file_name

    def get_top_restaurants(self, criteria: RestaurantCriteria) -> Set[Restaurant]:
        '''
        Given a set of criteria, returns the top 5 Restaurants which satisfy
        the criteria.
        '''
        valid_restaurants = self.determine_valid_restaurants(criteria)
        return self._get_top_restaurants(valid_restaurants)

    def determine_valid_restaurants(self, criteria: RestaurantCriteria) -> Set[Restaurant]:
        '''
        Parses the Cuisine and Restaurant CSVs, turning the Restaurants into
        objects and returning all of the restaurants which conform to the given
        Criteria. Ensures that files are being read from the /csv file.
        '''

        cuisines = self._build_cuisines_map()
        restaurants: Set[Restaurant] = set()

        with open('csv/'+self.restaurant_file_name, 'r') as csvfile:
            restaurant_reader = csv.DictReader(csvfile)
            for restaurant_dict in restaurant_reader:
                try:
                    restaurant: Restaurant = Restaurant(
                        name=restaurant_dict['name'],
                        customer_rating=int(
                            restaurant_dict['customer_rating']),
                        distance=float(restaurant_dict['distance']),
                        average_price=float(restaurant_dict['price']),
                        cuisine=cuisines[restaurant_dict['cuisine_id']]
                    )
                except:
                    raise ValueError(
                        f'Restaurant CSV csv/{self.restaurant_file_name} is incorrectly formatted')

                # Only add if the restaurant meets the criteria
                if self._is_valid_restaurant(restaurant, criteria):
                    restaurants.add(restaurant)
        return restaurants

    def display(self, restaurants: List[Restaurant]) -> None:
        '''
        Provides a command line table view of the given restaurants
        '''

        # Print table header
        print("\n{:<40}{:<20}{:<15}{:<19}{:<8}".format(
            'Name', 'Rating (stars)', 'Distance (mi)', 'Avg. Price ($)', 'Cuisine'))

        for restaurant in restaurants:
            print("{:<40}{:<20}{:<15}{:<19}{:<8}".format(
                restaurant.name, restaurant.customer_rating,  restaurant.distance,  restaurant.average_price,  restaurant.cuisine))
        print('\n')

    def _is_valid_restaurant(self, restaurant: Restaurant, criteria: RestaurantCriteria) -> bool:
        '''
        Given a Restaurant and RestaurantCriteria, determine whether the
        restaurant conforms to the constraints. Every constraint filtered for
        (not None in the RestaurantCriteria) must be satisfied by the restaurant.
        '''

        valid_restaurant = RestaurantIsRatedWellEnough() & RestaurantIsCloseEnough(
        ) & RestaurantIsCheapEnough() & RestaurantIsTheRightCuisine() & RestaurantIsTheRightName() & RestaurantIsTheRightName()
        return valid_restaurant.is_satisfied_by(restaurant, criteria)

    def _get_top_restaurants(self, restaurants: Set[Restaurant]) -> List[Restaurant]:
        '''
        Given a set of restaurants, sorts the restaurants by closest distance,
        breaking ties with largest customer rating, and further breaking ties
        by average_price. Returns, at max, the first five elements of the sorted list. 
        '''

        top_restaurants = sorted(restaurants, key=lambda r: (
            r.distance, -r.customer_rating, r.average_price))

        if len(top_restaurants) > 5:
            top_restaurants = top_restaurants[0:5]

        return top_restaurants

    def _build_cuisines_map(self):
        '''From the CSV, builds a map of id=>name for faster lookups'''
        cuisine_map: Dict[str, str] = {}
        with open('csv/'+self.cuisine_file_name, 'r') as csvfile:
            cuisine_reader = csv.DictReader(csvfile)
            for cuisine in cuisine_reader:
                try:
                    cuisine_map[cuisine.get('id')] = cuisine.get('name')
                except:
                    raise ValueError(
                        f'Cuisines CSV csv/{self.cuisine_file_name} is incorrectly formatted')
        return cuisine_map
