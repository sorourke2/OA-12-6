from typing import Optional
from specifications.base_specification import BaseSpecification
from models.restaurant import Restaurant
from models.restaurant_criteria import RestaurantCriteria


class RestaurantIsTheRightName(BaseSpecification):
    def is_satisfied_by(self, restaurant: Restaurant, criteria: RestaurantCriteria) -> bool:
        '''Is satisfied if the name of the restaurant partially matches the criteria's'''

        return strings_partially_match(restaurant.name, criteria.restaurant_name)


class RestaurantIsTheRightCuisine(BaseSpecification):
    def is_satisfied_by(self, restaurant: Restaurant, criteria: RestaurantCriteria) -> bool:
        '''Is satisfied if the cuisine of the restaurant partially matches the criteria's'''

        return strings_partially_match(restaurant.cuisine, criteria.cuisine)


class RestaurantIsCheapEnough(BaseSpecification):
    def is_satisfied_by(self, restaurant: Restaurant, criteria: RestaurantCriteria) -> bool:
        '''Is satisfied if the average price is <= the criteria's max price. '''

        if criteria.max_price is not None:
            return restaurant.average_price <= criteria.max_price
        return True


class RestaurantIsRatedWellEnough(BaseSpecification):
    def is_satisfied_by(self, restaurant: Restaurant, criteria: RestaurantCriteria) -> bool:
        '''Is satisfied if the restaurant's rating is >= the criteria's min rating. '''

        if criteria.min_customer_rating is not None:
            return restaurant.customer_rating >= criteria.min_customer_rating
        return True


class RestaurantIsCloseEnough(BaseSpecification):
    def is_satisfied_by(self, restaurant: Restaurant, criteria: RestaurantCriteria) -> bool:
        '''Is satisfied if the restaurant's distance is <= the criteria's max distance. '''

        if criteria.max_distance is not None:
            return restaurant.distance <= criteria.max_distance
        return True


def strings_partially_match(to_match_against: str, string_to_match_with: Optional[str]) -> bool:
    """
    Determines if the string to_match_against has any words prefixed with string_to_match_with.
    When the match_with string is None or empty, the strings match.
    """

    if not string_to_match_with:
        return True

    lowercase_match = string_to_match_with.lower()
    lowercase_given = to_match_against.lower()

    # Determine if there is a partial match
    all_words_in_name = lowercase_given.split(' ')
    for word in all_words_in_name:
        if word.startswith(lowercase_match):
            return True
    return False
