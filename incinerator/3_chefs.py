from operator import setitem as s

add = lambda a: lambda x, y, z: s(x.__dict__, a, x.__dict__.get(a, 0) + y * z)

class A:
    add_food, add_drink = map(add, 'fd')
    total = lambda s: f'{s.F}: {s.f}, {s.D}: {s.d}, Total: {s.f + s.d}'

cook = lambda F,D: type('', (A,), locals())

JapaneseCook = cook('Sushi', 'Tea')
RussianCook = cook('Dumplings', 'Compote')
ItalianCook = cook('Pizza', 'Juice')