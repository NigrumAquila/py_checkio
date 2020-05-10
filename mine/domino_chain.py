def domino_chain(tiles: str) -> int:
    tiles = set(tiles.replace(",", "").split())
    starts = {tile for tile in tiles} | {tile[::-1] for tile in tiles}
    lines = []

    for start in starts:
        ln = start
        tl = start if start in tiles else start[::-1]
        stack = [(ln, tiles - {tl})]

        while stack:  
            line, rest = stack.pop(0)
            if not rest:
                if line[::-1] not in lines:
                    lines.append(line)
                continue

            last = line[-1]
            nbs = [r for r in rest if last in [r[0], r[-1]]]
            for nb in nbs:
                app = nb if nb[0] == last else nb[::-1]
                stack.append((f"{line} {app}", rest - {nb}))

    return len(lines)