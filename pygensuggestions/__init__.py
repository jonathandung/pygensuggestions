# Copyright © 2026 Jonathan Dung. All rights reserved.
# SPDX-License-Identifier: MIT
"""Provides a `suggest` function that returns the closest match from a list of candidate strings to a target string under a specific, fine-tuned metric.
Do read through the source code if you are curious, but note that the main logic is in `pygensuggestions/lib.py`.
"""

from pygensuggestions import lib

__all__ = ('suggest',)
__version__ = '2.3.2'


def suggest(z, i, /, *, skip_identical=True, respect_bounds=True):
    """Return the closest match from the candidates given a list of candidate strings and a target string.
    Pass `skip_identical=False` to allow the function to return the target string if it is present in the candidates, and `respect_bounds=False`
    to disable the limits on the number of candidate items and the length of the target string (may cause unexpected behaviour).
    """
    b = x = len(i)
    if respect_bounds and (
        len(z) >= lib.MAX_CANDIDATE_ITEMS or x > lib.MAX_STRING_SIZE
    ):
        return
    s = None
    for c in z:
        if c == i:
            if skip_identical:
                continue
            return c
        m = min((len(c) + x) // 3 + 1, b - 1)
        d = lib.lev_dist(i, c, m)
        if m != d < b:
            s, b = c, d
    return s
