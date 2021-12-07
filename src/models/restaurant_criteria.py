
from typing import Optional
from dataclasses import dataclass


@dataclass
class RestaurantCriteria():
    '''
    Represents a set of criteria to compare a Restaurant to. Criteria is
    optional and thus fields not being filtered for are None.
    '''
    restaurant_name: Optional[str]
    max_distance: Optional[float]
    max_price: Optional[str]
    min_customer_rating: Optional[int]
    cuisine: Optional[str]
