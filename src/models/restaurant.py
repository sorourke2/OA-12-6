
from dataclasses import dataclass


@dataclass(frozen=True)
class Restaurant:
    '''Represents a Restaurant'''
    name: str
    customer_rating: int
    distance: float
    average_price: float
    cuisine: str
