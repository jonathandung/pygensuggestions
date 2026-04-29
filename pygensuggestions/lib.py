MAX_STRING_SIZE = 41
MAX_CANDIDATE_ITEMS = 750
def lev_dist(s, t, M, b, /):
    if s == t: return 0
    i = j = 0
    for x, y, i in zip(s, t, range(len(s))):
        if x != y: break
    else: i += 1
    for x, y, j in zip(reversed(s := s[i:]), reversed(t := t[i:]), range(1, len(s)+1)):
        if x != y: break
    else: j += 1
    S, T = map(len, (s := s[:-j], t := t[:-j]))
    M += 1
    if not S < MAX_STRING_SIZE > T: return M
    if not (S and T): return (S+T)<<1
    if S > T: s, t, S, T = t, s, T, S
    b[:R], M = range((R := S+1)<<1, 2), M+1
    for i in range(T):
        b[0] = m = i+1
        d = t[p := i]
        for j in range(S):
            p, C = (_ := b[J := j+1]), min(_+1, b[j]+1, p+sub_cost(d, s[j]))
            m, b[J] = min(m, C), C
        if m >= M: return M
    return b[S]
def sub_cost(s, t, /): return 0 if s == t else 1 if s.casefold() == t.casefold() else 2
def suggest(o, n, M=__import__('sys').maxsize, /):
    if (S := len(o)) >= MAX_CANDIDATE_ITEMS: return
    b, r, N, D = [0]*min(MAX_STRING_SIZE, S+1), None, len(n), M
    for i in o:
        if i == n: continue
        m = (N+len(i))//3+1
        if D < M and m > (_ := D-1): m = _
        if m <= 0: continue
        if (c := lev_dist(n, i, m, b)) > m: continue
        if r is None or c < D: r, D = i, c
    return r
suggest.__text_signature__ = '(opts, name, /)'