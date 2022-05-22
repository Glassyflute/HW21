from abc import ABC, abstractmethod


class Storage(ABC):
    # @property
    # @abstractmethod
    # def items(self):
    #     """
    #     items (словарь название:количество)
    #     :return:
    #     """
    #     pass
    #
    # @property
    # @abstractmethod
    # def capacity(self):
    #     """
    #     capacity (целое число)
    #     :return:
    #     """
    #     pass

    @abstractmethod
    def add(self, item, quantity):
        """
        add(<название>, <количество>) - увеличивает запас items
        :return:
        """
        pass

    @abstractmethod
    def remove(self, item, quantity):
        """
        remove(<название>, <количество>) - уменьшает запас items
        :return:
        """
        pass

    @abstractmethod
    def get_free_space(self):
        """
        get_free_space() - вернуть количество свободных мест
        :return:
        """
        pass

    @abstractmethod
    def get_items(self):
        """
        get_items() - возвращает сожержание склада в словаре {товар: количество}
        :return:
        """
        pass

    @abstractmethod
    def get_unique_items_count(self):
        """
        get_unique_items_count() - возвращает количество уникальных товаров.
        :return:
        """
        pass


class Store(Storage):
    def __init__(self):
        self._items = {}
        self._capacity = 100

    @property
    def items(self):
        return self._items

    @property
    def capacity(self):
        return self._capacity

    # getters, setters ???? нужны или нет далее посмотреть

    def add(self, item, quantity):
        if quantity <= self.get_free_space():
            print(f"Свободных слотов: {self.get_free_space()}, хотим занять {quantity}")

            if item in self._items:
                slots_taken_per_good = self._items[item]
                # если товар уже есть в наличии, то корректируем его кол-во.
                if slots_taken_per_good:
                    slots_taken_per_good += int(quantity)
                    self._items[item] = slots_taken_per_good
                    print(f"Товар {item} добавлен в кол-ве {quantity}. Итого для {item} занято слотов: {slots_taken_per_good}")
                    return self._items
                    # clarify which return is needed and is convenient

            # если товара нет в наличии, добавляем указанное кол-во.
            self._items[item] = int(quantity)
            print(f"Товар {item} добавлен в кол-ве {quantity}. Итого для {item} занято слотов: {quantity}")
            return self._items
        else:
            return f"Недостаточно места для добавления товара. Уменьшите количество товара."

    def remove(self, item, quantity):
        if item in self._items:
            slots_taken_per_good = self._items[item]
            # если есть товар в наличии, смотрим на достаточность имеющегося кол-ва.
            if slots_taken_per_good:
                if quantity <= slots_taken_per_good:
                    slots_taken_per_good -= int(quantity)
                    self._items[item] = slots_taken_per_good
                    print(f"Товар {item} снижен в кол-ве {quantity}. Итого для {item} занято слотов: {slots_taken_per_good}")

                    # если кол-во товара снижено до нуля, убираем вид товара (ключ из словаря),
                    # чтобы можно было добавить другой вид товара.
                    if slots_taken_per_good == 0:
                        del self._items[item]

                    return self._items
                else:
                    return "Количество товара недостаточно для проведения операции."

        # если товара нет в наличии
        return "Такого товара нет в наличии."

    def get_free_space(self):
        storage_space_taken = 0
        for item_name in self._items:
            slots_taken_per_good = self._items[item_name]
            storage_space_taken += slots_taken_per_good

        space_available = self._capacity - storage_space_taken
        return space_available

    def get_items(self):
        for item_key, item_value in self._items.items():
            print(f"{item_value} {item_key}")
        return self._items

    def get_unique_items_count(self):
        return len(self._items.keys())


class Shop(Store):
    def __init__(self):
        self._items = {}
        self._capacity = 20

    @property
    def items(self):
        return self._items

    @property
    def capacity(self):
        return self._capacity

    def add(self, item, quantity):
        # проверяем наличие свободных слотов для добавления товара.
        if quantity <= self.get_free_space():
            print(f"Свободных слотов: {self.get_free_space()}, хотим занять {quantity}")

            # проверяем, имеется ли уже товар в магазине.
            # добавляем товар, если в магазине менее 5 различных видов товара.
            # Иначе выводим предупреждения о превышении лимита по видам товара.
            if item not in self._items:
                # для нового вида товара проверяем, позволяет ли лимит добавление в магазин.
                if self.get_unique_items_count() >= 5:
                    return "Невозможно добавить товар, т.к. будет превышен лимит по кол-ву видов товаров."

                self._items[item] = int(quantity)
                print(f"Товар {item} добавлен в кол-ве {quantity}. Итого для {item} занято слотов: {quantity}")
                return self._items

            # если товар уже есть в наличии, то корректируем его кол-во.
            if item in self._items:

                slots_taken_per_good = self._items[item]
                if slots_taken_per_good:
                    slots_taken_per_good += int(quantity)
                    self._items[item] = slots_taken_per_good
                    print(f"Товар {item} добавлен в кол-ве {quantity}. Итого для {item} занято слотов: {slots_taken_per_good}")
                    return self._items

        else:
            return f"Недостаточно места для добавления товара. Уменьшите количество товара."

    def remove(self, item, quantity):
        super().remove(item, quantity)
        # none === 80 slots

        # if item in self._items:
        #
        #     slots_taken_per_good = self._items[item]
        #     # если есть товар в наличии, смотрим на достаточность имеющегося кол-ва.
        #     if slots_taken_per_good:
        #         if quantity <= slots_taken_per_good:
        #             slots_taken_per_good -= int(quantity)
        #             self._items[item] = slots_taken_per_good
        #             print(f"Товар {item} снижен в кол-ве {quantity}. Итого для {item} занято слотов: {slots_taken_per_good}")
        #
        #             # если кол-во товара снижено до нуля, убираем вид товара (ключ из словаря),
        #             # чтобы можно было добавить другой вид товара.
        #             if slots_taken_per_good == 0:
        #                 del self._items[item]
        #
        #             return self._items
        #         else:
        #             return "Количество товара недостаточно для проведения операции."
        #
        # # если товара нет в наличии
        # return "Такого товара нет в наличии."

    # def get_free_space(self):
    #     storage_space_taken = 0
    #     for item_name in self._items:
    #         slots_taken_per_good = self._items[item_name]
    #         storage_space_taken += slots_taken_per_good
    #
    #     space_available = self._capacity - storage_space_taken
    #     return space_available
    #
    # def get_items(self):
    #     return self._items
    #
    # def get_unique_items_count(self):
    #     return len(self._items.keys())


class Request:
    def __init__(self, input_str):
        data = input_str.split(" ")
        # "Доставить 3 печеньки из склад в магазин"

        self.from_value = data[4]
        self.to_value = data[6]
        self.amount = int(data[1])
        self.product = data[2]

    def __repr__(self):
        return f"Доставить {self.amount} {self.product} из {self.from_value} в {self.to_value}"


