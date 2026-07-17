from . import lib # ruff: ignore[unused-import]
from collections.abc import Iterable, Sized
from ty_extensions import Intersection
from typing import AnyStr, Final
__all__ = 'suggest',
def suggest(candidates: Intersection[Sized, Iterable[AnyStr]], item: AnyStr, /, *, skip_identical: bool = True, respect_bounds: bool = True) -> AnyStr|None: ...
__version__: Final[str]
