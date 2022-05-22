from classes import Request, Store, Shop


if __name__ == "__main__":
    shop = Shop()
    store = Store()

    print(store.add("печеньки", 10))
    print(store.add("собачки", 5))
    print(store.add("коробки", 15))
    print(store.add("печеньки", 150))
    print(store.remove("печеньки", 10))

    print("В склад хранится:")
    print(store.get_items())
    print(f"Свободных слотов: {store.get_free_space()}")

    print("======== DIVIDER ============")
    print(shop.add("печеньки", 5))
    print(shop.add("собачки", 2))
    print(shop.add("коробки", 3))
    print(shop.add("кошки", 1))
    print(shop.add("котятки", 1))
    print(shop.add("кошки", 1))     # лимит в 5 видов достигнут. можем повысить кол-во имеющихся.
    print(shop.add("уточки", 1))    # пробуем добавить 6й товар при лимите в 5 видов
    print(shop.remove("печеньки", 5))
    print(shop.add("уточки", 1))


    print("В магазин хранится:")
    print(shop.get_items())
    print(f"Свободных слотов: {store.get_free_space()}")


    # user_input = input("Введите строку следующего типа: "
    #                    "'Доставить (количество) (наименование товара) из (место отправки) в (место доставки)'")
    #
    # fsdf










