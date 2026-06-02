__all__ = 'suggest',
from ._types import Candidates
from . import lib # noqa: F401
from typing import AnyStr, Final
def suggest(candidates: Candidates[AnyStr], item: AnyStr, /, *, skip_identical: bool = True, respect_bounds: bool = True) -> AnyStr|None: ...
__version__: Final[str]