#!/usr/bin/env python

import argparse
from typing import Any, List
from os.path import exists
from specifications.restaurant import RestaurantCriteria
from search_restaurants_program import FilterRestaurantsCSVProgram
from models.restaurant import Restaurant


def main(args) -> List[Restaurant]:

    criteria = RestaurantCriteria(
        restaurant_name=args.name,
        max_distance=args.distance,
        max_price=args.price,
        min_customer_rating=args.customer_rating,
        cuisine=args.cuisine
    )
    restaurant_file_name: str = args.restaurant_file
    cuisine_file_name: str = args.cuisine_file
    program = FilterRestaurantsCSVProgram(
        restaurant_file_name=restaurant_file_name, cuisine_file_name=cuisine_file_name)
    top_restaurants: List[Restaurant] = program.get_top_restaurants(criteria)
    program.display(top_restaurants)
    return top_restaurants


def make_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description='Filter and display CSV Recipe data given a set of criteria.')
    parser.add_argument('-f', '--restaurant-file', type=is_valid_csv_file,
                        help='Name of restaurant data csv located in src/csv. Must contain .csv', default='restaurants.csv')
    parser.add_argument('--cuisine-file', type=is_valid_csv_file,
                        help='Name of cuisines data csv located in src/csv. Must contain .csv', default='cuisines.csv')
    parser.add_argument(
        '-n',
        '--name',
        type=str,
        help='Prefix of one of the words in the name of the restaurant, ignores case when filtering',
    )
    parser.add_argument('-d', '--distance',
                        type=is_positive_float, help='Max distance in miles to the restaurant')
    parser.add_argument('--customer-rating', metavar="[1-5]", choices=range(1, 6),
                        type=int, help='Min customer rating out of 5 stars')
    parser.add_argument('-p', '--price',
                        type=is_positive_float, help='Max price in US dollars for the average price')
    parser.add_argument('-c', '--cuisine', type=str,
                        help='Prefix of one of the words in a cuisine name, ignores case when filtering')
    return parser


def is_positive_float(value: Any) -> bool:
    '''Determines if the value is a positive float, otherwise throws argparse error'''
    value = float(value)
    if value <= 0:
        raise argparse.ArgumentTypeError(
            f'{value} is an invalid positive float value')
    return value


def is_valid_csv_file(value: Any) -> bool:
    '''Determines if the value is a .csv file and exists in csv/, otherwise throws argparse error'''
    if not exists('csv/'+value):
        raise argparse.ArgumentTypeError(
            f'csv/{value} does not exist')
    if not value.endswith('.csv'):
        raise argparse.ArgumentTypeError(
            f'csv/{value} is not a CSV file')
    return value


if __name__ == '__main__':
    main(make_parser().parse_args())
