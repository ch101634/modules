def shopping(shop_file):
    shop_dict = {} # 생성할 사전 객체
    with open(data_path.name+'/'+shop_file) as f:
        for line in f:
            try:
                name, price = line.strip().split()
                price=int(price.replace('원', ''))
            except:
                pass
            if type(price)!=str:
                shop_dict[name] = price
    return shop_dict


def item_price(shop_file, item):
    shop_dict = {} # 생성할 사전 객체
    with open(data_path.name+'/'+shop_file) as f:
        for line in f:
            try:
                name, price = line.strip().split()
                price=int(price.replace('원', ''))
            except:
                pass
            if type(price)!=str:
                shop_dict[name] = price
    return shop_dict[item]
