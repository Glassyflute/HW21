def show_delivery_progress(item, quantity):
    """
    показывает стандартную информацию по процессу доставки выбранного товара.
    :param item: наименование товара
    :param quantity: кол-во товара
    :return:
    """
    return f"Курьер забрал {quantity} {item} со склад.\n" \
           f"Курьер везет {quantity} {item} со склад в магазин.\n" \
           f"Курьер доставил {quantity} {item} в магазин."


def show_items(store, shop):
    """
    показывает информацию по наличию товаров на складе и в магазине.
    :param store: склад
    :param shop: магазин
    :return:
    """
    return f"В склад хранится:\n{store.get_items()}\n" \
           f"Свободных слотов: {store.get_free_space()}\n" \
           f"В магазин хранится:\n{shop.get_items()}\n" \
           f"Свободных слотов: {shop.get_free_space()}"


