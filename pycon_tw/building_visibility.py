from collections import namedtuple


Point = namedtuple('Point', 'x y')


class Rect(namedtuple('Rect', 'p1 p2 z key')):

    @property
    def area(self):
        return (self.p2.x - self.p1.x) * (self.p2.y - self.p1.y)

    def intersection(self, other):
        if self.p2.x <= other.p1.x or other.p2.x <= self.p1.x or \
                        self.p2.y <= other.p1.y or other.p2.y <= self.p1.y:
            return None
        return Rect(
            Point(max(self.p1.x, other.p1.x), max(self.p1.y, other.p1.y)),
            Point(min(self.p2.x, other.p2.x), min(self.p2.y, other.p2.y)),
            self.z, self.key)

    def diff(self, other):
        other = self.intersection(other)
        if other is None:
            return [self]
        result = [
            Rect(self.p1, other.p1, self.z, self.key),
            Rect(Point(self.p1.x, other.p1.y), Point(other.p1.x, other.p2.y), self.z, self.key),
            Rect(Point(self.p1.x, other.p2.y), Point(other.p1.x, self.p2.y), self.z, self.key),
            Rect(Point(other.p1.x, self.p1.y), Point(other.p2.x, other.p1.y), self.z, self.key),
            Rect(Point(other.p1.x, other.p2.y), Point(other.p2.x, self.p2.y), self.z, self.key),
            Rect(Point(other.p2.x, self.p1.y), Point(self.p2.x, other.p1.y), self.z, self.key),
            Rect(Point(other.p2.x, other.p1.y), Point(self.p2.x, other.p2.y), self.z, self.key),
            Rect(other.p2, self.p2, self.z, self.key),
        ]
        return [r for r in result if r.area > 0]


def checkio(buildings):
    rects = [Rect(Point(x1, 0), Point(x2, h), y1, i) for i, (x1, y1, x2, y2, h) in enumerate(buildings)]
    rects.sort(key=lambda r: r.z, reverse=True)
    visibles = []
    for rect1 in rects:
        res = []
        for rect2 in visibles:
            res.extend(rect2.diff(rect1))
        res.append(rect1)
        visibles = res
    return len({r.key for r in visibles})