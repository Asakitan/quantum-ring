"""Exact small-ring observability checks. Python 3.9+."""
from math import gcd


def observability_rows(n, wrap):
    # One real signed bond is gauge-equivalent to total flux 0 or pi.
    sites = []
    for x in range(n):
        v = [int(i == x) for i in range(n)]
        rows = []
        for _ in range(n):
            rows.append(v)
            v = [(wrap if i == 0 else 1)*v[(i-1) % n] +
                 (wrap if i == n-1 else 1)*v[(i+1) % n] for i in range(n)]
        sites.append(rows)
    return sites


def full_rank(sites, mask, n):
    pivots = {}
    for x in range(n):
        if not (mask >> x & 1):
            continue
        for row in sites[x]:
            v = row
            for i in range(n):
                if not v[i]:
                    continue
                if i not in pivots:
                    pivots[i] = v
                    break
                w = pivots[i]
                v = [w[i]*a-v[i]*b for a, b in zip(v, w)]
                g = gcd(*v)
                if g > 1:
                    v = [a//g for a in v]
            if len(pivots) == n:
                return True
    return False


def rings():
    masks = total_r = 0
    for n in range(3, 11):
        p = next(i for i in range(2, n+1) if n % i == 0)
        signed = [observability_rows(n, wrap) for wrap in (1, -1)]
        damage = [0] * (1 << n)
        for mask in range(1, 1 << n):
            X = [x for x in range(n) if mask >> x & 1]
            ok = all(full_rank(rows, mask, n) for rows in signed)
            if ok != (gcd(n, *(x-X[0] for x in X)) == 1):
                raise AssertionError((n, X, ok))
            if ok:
                damage[mask] = 1 + min(damage[mask ^ (1 << x)] for x in X)
            masks += 1
        for r in range(n+1):
            m = (p*(r+1) + p-2)//(p-1)
            actual = min((bin(i).count("1") for i, d in enumerate(damage) if d > r),
                         default=None)
            if actual != (m if m <= n else None) or (m <= n and damage[2**m-1] <= r):
                raise AssertionError((n, r, actual, m))
            total_r += 1
    print(f"rings: N=3..10, nonempty_masks={masks}, (N,r)_cases={total_r}, exact ranks OK")


if __name__ == "__main__":
    rings()
