from typing import Any
from abc import abstractmethod
from dataclasses import dataclass


class BaseSpecification:
    '''
    An abstract object providing the functionality of determining whether
    an object satsifies some condition. Supports the combining of Specifications
    to create more complex boolean expressions. Overrides the __call__ method
    to allow this functionality.
    '''
    @abstractmethod
    def is_satisfied_by(self, candidate: Any, criteria: Any) -> bool:
        raise NotImplementedError()

    def __call__(self, candidate: Any, criteria: Any) -> bool:
        return self.is_satisfied_by(candidate, criteria)

    def __and__(self, other: "BaseSpecification") -> "AndSpecification":
        return AndSpecification(self, other)

    def __or__(self, other: "BaseSpecification") -> "OrSpecification":
        return OrSpecification(self, other)

    def __neg__(self) -> "NotSpecification":
        return NotSpecification(self)


@dataclass(frozen=True)
class AndSpecification(BaseSpecification):
    '''Represents the binary comparison of two specifications with an and expression'''
    left: BaseSpecification
    right: BaseSpecification

    def is_satisfied_by(self, candidate: Any, criteria: Any) -> bool:
        return self.left.is_satisfied_by(candidate, criteria) and self.right.is_satisfied_by(candidate, criteria)


@dataclass(frozen=True)
class OrSpecification(BaseSpecification):
    '''Represents the binary comparison of two specifications with an or expression'''
    left: BaseSpecification
    right: BaseSpecification

    def is_satisfied_by(self, candidate: Any, criteria: Any) -> bool:
        return self.left.is_satisfied_by(candidate, criteria) or self.right.is_satisfied_by(candidate, criteria)


@dataclass(frozen=True)
class NotSpecification(BaseSpecification):
    '''Represents the negation of one specification with a not expression'''
    specification: BaseSpecification

    def is_satisfied_by(self, candidate: Any, criteria: Any) -> bool:
        return not self.specification.is_satisfied_by(candidate, criteria)
