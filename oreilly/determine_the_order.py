from collections import defaultdict


def DFS(G, v, seen=None, path=None):
    if seen is None: seen = []
    if path is None: path = [v]
    seen.append(v)
    paths = []
    for t in G[v]:
        if t not in seen:
            t_path = path + [t]
            paths.append(tuple(t_path))
            paths.extend(DFS(G, t, seen[:], t_path))
    return paths


def make_pairs(words):
    res = []
    for word in words:
        res.extend(list(word[i:i + 2]) for i in range(len(word) - 1))
    return res


def checkio(words):
    edges = make_pairs(words)
    G = defaultdict(list)
    for (s, t) in edges:
        G[s].append(t)
    all_paths = [p for ps in [DFS(G, n) for n in set(G)] for p in ps]
    if not all_paths:
        uniq_chars = ''.join(set(''.join(words)))
        return ''.join(sorted(uniq_chars))
    max_len = max(len(p) for p in all_paths)
    all_chars = set().union(*words)
    max_paths = [p for p in all_paths if len(p) == max_len]
    chains = set(max_paths)
    if len(all_chars) != max_len:
        res = []
        if len(chains)>2 and all(len(set(x))==len(x) for x in zip(*chains)):
            return ''.join(sorted(all_chars))
        for pairs in zip(*chains):
            if len(set(pairs)) != 1:
                res.extend(sorted(pairs))
            else:
                res.append(pairs[0])
        return ''.join(res)

    return ''.join(max_paths[0])