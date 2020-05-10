def bigger_price(limit: int, data: list) -> list:
    data = sorted(data, key=lambda k: -k['price'])
    while(len(data) != limit):
        data.pop();
    return data;