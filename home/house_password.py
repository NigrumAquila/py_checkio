def checkio(data: str) -> bool:
    if len(data) < 10:
      return False;
    if not (any(c.islower() for c in data) and any(c.isupper() for c in data) and any(c.isdigit() for c in data)):
        return False;
    return True;