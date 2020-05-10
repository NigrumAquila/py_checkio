def two_teams(sailors):
    return [
        sorted([k for k,v in sailors.items() if v<20 or v>40]),
        sorted([k for k,v in sailors.items() if 40>=v>=20])
    ]