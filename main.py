from classes import Request, Store, Shop
from utils import show_delivery_progress, show_items
proceed_further = True

if __name__ == "__main__":
    store = Store()
    store.items = {"печеньки": 10, "собачки": 5, "коробки": 25, "котики": 20}

    shop = Shop()
    shop.items = {"печеньки": 5, "собачки": 5}

    # print(show_items(store, shop))

    while proceed_further:

        user_input = input("Введите строку следующего типа: "
                           "'Доставить (количество) (наименование товара) из (место отправки) в (место доставки)'\n")
        if user_input == "stop":
            break

        user_request = Request(user_input)
        print(user_request)

        # примеры:
        # Дайте 3 печеньки из склад в магазин === ОК, Нужное количество есть на складе
        # Привезите 7 собачки из склад в магазин == ожидаем: Не хватает на складе
        # Привезите 15 коробки из склад в магазин = ожидаем: В магазине недостаточно места

        store_result = store.remove(user_request.product, user_request.amount)
        # print(f"store_result - {store_result}")
        if True in store_result:
            print("Нужное количество товара есть в наличии.")
            shop_result = shop.add(user_request.product, user_request.amount)
            # print(f"shop_result - {shop_result}")
            if True in shop_result:
                print("Нужное количество товара будет добавлено.")
                print(show_delivery_progress(user_request.product, user_request.amount))
                print(show_items(store, shop))
            else:
                print("Недостаточно места для добавления товара. Советуем изменить заказ.")
        else:
            print("Не хватает товара в наличии. Советуем изменить заказ.")


