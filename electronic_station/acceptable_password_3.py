def is_acceptable_password(password: str) -> bool:
    return len(password) > 6 and any(map(str.isdigit, password)) and not password.isnumeric()