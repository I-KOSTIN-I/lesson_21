from classes import Request, Shop, Store


if __name__ == '__main__':
    shop = Shop()
    store = Store()

    store.add('печеньки', 3)
    store.add('собачки', 4)
    store.add('коробки', 5)

    print('На складе')
    print(store.get_items())

    user_input = input('Введите данные в таком формате: "Доставить 3 собачки из склад в магазин": \n')
    data_request = Request(user_input)

    result_store = store.remove(data_request.product, data_request.amount)
    if result_store:
        print(f'Курьер забрал {data_request.amount} {data_request.product} со склад')
        print(f'Курьер везет {data_request.amount} {data_request.product} со склад в магазин')
        result_shop = shop.add(data_request.product, data_request.amount)
        if not result_shop:
            store.add(data_request.product, data_request.amount)
        else:
            print(f'Курьер доставил {data_request.amount} {data_request.product} в магазин')

    print('На складе')
    print(store.get_items())

    print('В магазине')
    print(shop.get_items())
