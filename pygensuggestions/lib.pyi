from typing import AnyStr, Literal, TypeVar

__T = TypeVar('__T', int, str)

__all__ = 'MAX_CANDIDATE_ITEMS', 'MAX_STRING_SIZE', 'lev_dist', 'sub_cost'
MAX_STRING_SIZE: int
MAX_CANDIDATE_ITEMS: int

def lev_dist(s: AnyStr, t: AnyStr, n: int, /) -> int: ...
def sub_cost(s: __T, t: __T, /) -> Literal[0, 1, 2]: ...
