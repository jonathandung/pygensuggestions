__all__ = 'suggest',
from . import lib # noqa: F401
from collections.abc import Iterable, Sized
from ty_extensions import Intersection
from typing import AnyStr, Final
def suggest(candidates: Intersection[Sized, Iterable[AnyStr]], item: AnyStr, /, *, skip_identical: bool = True, respect_bounds: bool = True) -> AnyStr|None: ...
__version__: Final[str]
