def second_index(text: str, symbol: str) -> [int, None]:
    res = text.find(symbol, text.find(symbol) + 1)
    if(res != -1):
        return res;
    return None;