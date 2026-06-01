# Copyright © 2026 Jonathan Dung. All rights reserved.
# SPDX-License-Identifier: MIT
'''Provides a `suggest` function that returns the closest match from a list of candidate strings to a target string under a specific, fine-tuned metric.
Do read through the source code if you are curious, but note that the main logic is in `lib.py`.'''
__all__ = 'suggest',
from pygensuggestions import lib
def suggest(candidates, item, /, *, skip_identical=True, respect_bounds=True):
    '''The main feature of this library. Given a list of candidate strings and a target string, return the closest match from the candidates,
    or `None` if there is no good match.
    Pass `skip_identical=False` to allow the function to return the target string if it is present in the candidates, and `respect_bounds=False`
    to disable the limits on the number of candidate items and the length of the target string (may cause unexpected behaviour).'''
    b = x = len(item)
    if respect_bounds and (len(candidates) >= lib.MAX_CANDIDATE_ITEMS or x > lib.MAX_STRING_SIZE): return # pragma: no branch
    s = None
    for c in candidates:
        if c == item:
            if skip_identical: continue
            return c
        m = min((len(c)+x)//3+1, b-1)
        d = lib.lev_dist(item, c, m)
        if d == m: continue # pragma: no branch
        if d < b: s, b = c, d
    return s
__version__ = '1.3.0'