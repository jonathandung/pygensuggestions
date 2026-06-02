from argparse import ArgumentParser
from collections.abc import Iterable
from typing import Final, Literal
parser: Final[ArgumentParser]
def main(argv: Iterable[str] | None = None) -> Literal[0, 1, 2, 3, 4]: ...