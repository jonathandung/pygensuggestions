__all__ = 'MAX_CANDIDATE_ITEMS', 'MAX_STRING_SIZE', 'lev_dist', 'sub_cost', 'suggest'
MAX_STRING_SIZE, MAX_CANDIDATE_ITEMS = 40, 750
def lev_dist(s, t, n, /, _=__import__('sys').maxsize): # noqa: B008
    i = j = 0
    x = y = None
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
            e[i] = r = min(d+sub_cost(c, s[i]), min(g, r)+2) # noqa: PLW2901
            d, m = g, min(m, r)
        if m >= n: return n
    return r
def sub_cost(s, t, /, a=65, z=90, d=32):
    if s == t: return 0
    if isinstance(s, str):
        if isinstance(t, str): return 1 if s.casefold() == t.casefold() else 2
        raise ValueError # pragma: no cover
    if not all(map(int.__instancecheck__, (s, t))): raise ValueError # pragma: no branch
    if a <= s <= z: s += d
    if a <= t <= z: t += d
    return 1 if s == t else 2
def suggest(o, n, /):
    b = x = len(n)
    if len(o) >= MAX_CANDIDATE_ITEMS or x > MAX_STRING_SIZE: return
    s = None
    for c in o:
        if c == n: continue
        d = lev_dist(n, c, min((len(c)+x)//3+1, b-1))
        if d < b: s, b = c, d
    return s
suggest.__text_signature__ = '(candidates, item, /)' # ty: ignore[unresolved-attribute]