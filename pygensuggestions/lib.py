'''Functions used by `suggest`, containing the core suggestion logic.'''
__all__ = 'MAX_CANDIDATE_ITEMS', 'MAX_STRING_SIZE', 'lev_dist', 'sub_cost'
MAX_STRING_SIZE = 40
'''The maximum length of the target string, past which the function always returns `None`. Though this is in all caps, signifying a constant,
that is just because the C implementation we're trying to copy declares this as a macro.'''
MAX_CANDIDATE_ITEMS = 750
'''The maximum number of candidate items, past which the function returns `None` indiscriminately. The same remark applies here as for `MAX_STRING_SIZE`.'''
def lev_dist(s, t, n, /, _=__import__('sys').maxsize): # ruff: ignore[function-call-in-default-argument]
    '''Return `n` or the (weighted) Levenshtein distance between `s` and `t`, whichever is smaller. As in the C version, `n` is required to allow early termination.'''
    i = j = 0
    for x, y, i in zip(s, t, range(len(s))):
        if x != y: break
    else: i += 1
    f = slice(i, None)
    s, t = s[f], t[f]
    for x, y, j in zip(reversed(s), reversed(t), range(1, len(s)+1)):
        if x != y: break
    else: j += 1
    f = slice(-j)
    s, t = s[f], t[f]
    a, b = map(len, (s, t))
    if not a <= MAX_STRING_SIZE >= b: return n # pragma: no branch
    if not (a and b): return (a+b)<<1
    if a > b: s, t, a, b = t, s, b, a
    e, n, r = list(range(2, 1+a<<1, 2)), n+1, 0
    for c, r in zip(t, range(0, b<<1, 2)):
        d, m = r, _
        for i in range(a):
            g = e[i]
            e[i] = r = min(d+sub_cost(c, s[i]), min(g, r)+2) # ruff: ignore[redefined-loop-name]
            d, m = g, min(m, r)
        if m >= n: return n
    return r
def sub_cost(s, t, /, a=65, z=90, d=32):
    '''The cost to substitute `s` for `t`, considering case.'''
    if s == t: return 0
    if isinstance(s, str):
        if isinstance(t, str): return 1 if s.casefold() == t.casefold() else 2
        raise TypeError # pragma: no cover
    if not (isinstance(s, int) and isinstance(t, int)): raise TypeError # pragma: no branch
    if a <= s <= z: s += d
    if a <= t <= z: t += d
    return 1 if s == t else 2
lev_dist.__text_signature__, sub_cost.__text_signature__ = '(s, t, n, /)', '(s, t, /)' # ty: ignore[unresolved-attribute]
