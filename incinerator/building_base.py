class Building:
    def __init__(s,x,y,a,b,h=10): s.x,s.y,s.a,s.b,s.h=x,y,a,b,h
    __repr__ = lambda s: "Building({}, {}, {}, {}, {})".format(s.x,s.y,s.a,s.b,s.h)
    area,volume = lambda s: s.a*s.b,lambda s: s.a*s.b*s.h
    corners = lambda s: {"south-west":(s.x,s.y),"north-east":(s.x+s.b,s.y+s.a),
                        "south-east":(s.x,s.y+s.a),"north-west":(s.x+s.b,s.y)}