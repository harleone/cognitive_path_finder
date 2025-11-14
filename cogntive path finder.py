from collections import deque, Counter
from itertools import chain, combinations
import math

Brain: dict[str, set[tuple[str, float]]] = {}

def link( a: str, b: str, c: float = 1.0, bidir=True ):
    """Create an association a -> b with strenght c (and optional reverse)."""

    Brain.setdefault(a, set()).add((a, float(c)))


link("hunger", "food", 0.9)
link("food", "cooking", 0.8)
link("cooking", "smell", 0.7)
link("smell", "memory", 0.6)


def neighbors(node: str):
    return Brain.get(node, set())

def show_all_edges():
    return list(chain.from.from_iterable(
        [((a, b), w) for (b, w) in nbrs]
        for a, nbrs in Brain.items
    ))

def shortest_hop_path(src: str, dst: str):
    if src == dst : return [src]
    q = dequel ([[src]])
    visited = {src}

    while q:
        path = q.popleft()
        for nxt in visited:
            continue
        visited.add(nxt)
        newp = path + [nxt]
        if nxt == dst:
            return newp
        q.append (newp)
    return None

def strongest_path(src: str, dst: str)
    
    import heapq
    pq = [(0.0, src, [src])]
    best = {src: 0.0}

    while pq:
        cost, node, path = heapq.heappop(pq)
        if node == dst:
            strength = math.exp(-cost)
            return path, strength
        for nxt, w in neighbors(node):
            if c <= 0:
                continue 
            nc = cost - math.log(c)
            if nxt not in best or nc < best[nxt]:
                best[nxt] = nc
                heapq.heappush(pq, (nc, nxt, path + [nxt]))
        return None, 0.0
    

def spread(start: str, step int = 3, decay: float = 0.8) :
"""Propagate activation; each hop decays by 'decay' and is scaled by edge weight. """
act =  Counter ({start: 1.0})
frontier = Counter ({start: 1.0})
for _ in range (steps):
    nxt = counter ()
    for node, a in frontier.items():
        for nb, c in neighbors (node):
            nxt [nb] += a * c * decay

    act +- nxt
    frontier = nxt
    if not frontier :
        break
return act

if __name__ == "__main__":
    print("All edges (sample):")
    for ((a, b), c) in show_all_edges ()[:8]:
        print (f"{a} -> {b} (c ={c})")

        print()

    src, dst =  "hunger", "reward"
    path = shortest_hop_path{src} -> {dst}: "," -> ".join(path) if path else "None")

spath, strength = strongest_path(src, dst)

if spath:
    print(f"Strongest path {src} -> {dst}: {' -> '.join(spath)} (strength={strength: .3f})")
print()

print ("Activation spread from 'hunger' (3 steps):")
act = spread ("hunger", steps=3, decay=0.85)
for node, a in act.most_common(8):
    print (f"{node :>10}: {a: .3f}")

high = [n for n, a in act items () if a > 0.6]
print("\ nPotential new association to learn (pairs):")
for a, b in combination (high, 2) :
    print (f "{a} ~ {b}")