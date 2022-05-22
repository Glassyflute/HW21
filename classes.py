from abc import ABC, abstractmethod


class Storage(ABC):
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

    @items.setter
    def items(self, items_dict):
        self._items = items_dict

    @capacity.setter
    def capacity(self, capacity_value):
        self._capacity = capacity_value

    def __repr__(self):
        return "склад"

    def add(self, item, quantity):
        # проверяем наличие свободных слотов
        if quantity <= self.get_free_space():

            if item in self._items:
                slots_taken_per_good = self._items[item]
                # если товар уже есть в наличии, то корректируем его кол-во.
                if slots_taken_per_good:
                    slots_taken_per_good += int(quantity)
                    self._items[item] = slots_taken_per_good
                    operation_successful = True
                    return self._items, operation_successful, "Нужное количество товара будет добавлено."

            # если товара нет в наличии, добавляем указанное кол-во.
            self._items[item] = int(quantity)
            operation_successful = True
            return self._items, operation_successful, "Нужное количество товара будет добавлено."
        else:
            operation_successful = False
            return operation_successful, "Недостаточно места для добавления товара. Попробуйте что-то другое."

    def remove(self, item, quantity):
        if item in self._items:
            slots_taken_per_good = self._items[item]
            # если есть товар в наличии, смотрим на достаточность имеющегося кол-ва.
            if slots_taken_per_good:
                if quantity <= slots_taken_per_good:
                    slots_taken_per_good -= int(quantity)
                    self._items[item] = slots_taken_per_good

                    # если кол-во товара снижено до нуля, убираем вид товара (ключ из словаря),
                    # чтобы можно было добавить другой вид товара.
                    if slots_taken_per_good == 0:
                        del self._items[item]
                        operation_successful = True
                        return self._items, operation_successful, "Нужное количество товара есть в наличии."

                    operation_successful = True
                    return self._items, operation_successful, "Нужное количество товара есть в наличии."

                else:
                    operation_successful = False
                    return operation_successful, "Не хватает товара, попробуйте заказать меньше."

        # если товара нет в наличии
        operation_successful = False
        return operation_successful, "Такого товара нет в наличии."

    def get_free_space(self):
        storage_space_taken = 0
        for item_name in self._items:
            slots_taken_per_good = self._items[item_name]
            storage_space_taken += slots_taken_per_good

        space_available = self._capacity - storage_space_taken
        return space_available

    def get_items(self):
        return "\n".join([f"{item_value} {item_key}" for item_key, item_value in self._items.items()])

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

    @items.setter
    def items(self, items_dict):
        self._items = items_dict

    @capacity.setter
    def capacity(self, capacity_value):
        self._capacity = capacity_value

    def __repr__(self):
        return "магазин"

    def add(self, item, quantity):
        # проверяем наличие свободных слотов для добавления товара.
        if quantity <= self.get_free_space():

            # проверяем, имеется ли уже товар в магазине.
            # добавляем товар, если в магазине менее 5 различных видов товара.
            # Иначе выводим предупреждения о превышении лимита по видам товара.
            if item not in self._items:
                # для нового вида товара проверяем, позволяет ли лимит добавление в магазин.
                if self.get_unique_items_count() >= 5:
                    operation_successful = False
                    return operation_successful, "Невозможно добавить товар, т.к. будет превышен лимит по кол-ву" \
                                                 " видов товаров."

                self._items[item] = int(quantity)
                operation_successful = True
                return self._items, operation_successful, "Нужное количество товара будет добавлено."

            # если товар уже есть в наличии, то корректируем его кол-во.
            if item in self._items:
                slots_taken_per_good = self._items[item]
                if slots_taken_per_good:
                    slots_taken_per_good += int(quantity)
                    self._items[item] = slots_taken_per_good
                    operation_successful = True
                    return self._items, operation_successful, "Нужное количество товара будет добавлено."

        else:
            operation_successful = False
            return operation_successful, "Недостаточно места для добавления товара. Попробуйте что-то другое."

    def remove(self, item, quantity):

        if item in self._items:
            slots_taken_per_good = self._items[item]
            # если есть товар в наличии, смотрим на достаточность имеющегося кол-ва.
            if slots_taken_per_good:
                if quantity <= slots_taken_per_good:
                    slots_taken_per_good -= int(quantity)
                    self._items[item] = slots_taken_per_good

                    # если кол-во товара снижено до нуля, убираем вид товара (ключ из словаря),
                    # чтобы можно было добавить другой вид товара.
                    if slots_taken_per_good == 0:
                        del self._items[item]
                        operation_successful = True
                        return self._items, operation_successful, "Нужное количество товара есть в наличии."

                    operation_successful = True
                    return self._items, operation_successful, "Нужное количество товара есть в наличии."

                else:
                    operation_successful = False
                    return operation_successful, "Не хватает товара, попробуйте заказать меньше."

        # если товара нет в наличии
        operation_successful = False
        return operation_successful, "Такого товара нет в наличии."


class Request:
    def __init__(self, input_str):
        data = input_str.split(" ")
        # Строка формата: "Доставить 3 печеньки из склад в магазин"

        self.amount = int(data[1])
        self.product = data[2]

        if len(data) < 7:
            # по умолчанию товар доставляется со склада в магазин.
            self.from_value = "склад"
            self.to_value = "магазин"

        elif len(data) == 7:
            # в полной версии можно указать доставку по обоим направлениям.
            self.from_value = data[4]
            self.to_value = data[6]

    def __repr__(self):
        return f"Доставить {self.amount} {self.product} из {self.from_value} в {self.to_value}"

