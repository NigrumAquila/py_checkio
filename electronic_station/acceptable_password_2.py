def is_acceptable_password(password: str) -> bool:
    return len(password)>6 and len([c for c in password if c.isdigit()]) > 0