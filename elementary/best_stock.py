def best_stock(data):
    im = "";
    cost = 0;
    for name, price in data.items():
        if(cost < price):
            im = name;
            cost = price;
    return im;