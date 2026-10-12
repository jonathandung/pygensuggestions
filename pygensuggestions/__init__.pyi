from collections.abc import Iterable, Sized
from typing import AnyStr, Final

from ty_extensions import Intersection

from . import lib as lib

__all__ = ('suggest',)

def suggest(
    candidates: Intersection[Sized, Iterable[AnyStr]],
    item: AnyStr,
    /,
    *,
    skip_identical: bool = True,
    respect_bounds: bool = True,
) -> AnyStr | None: ...

__version__: Final[str]
