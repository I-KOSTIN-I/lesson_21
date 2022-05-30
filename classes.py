from abc import ABC, abstractclassmethod


class Storage:
    @abstractclassmethod
    def add(self, name, count):
        """(<название>, <количество>)  - увеличивает запас items"""
        pass

    @abstractclassmethod
    def remove(self, name, count):
        """(<название>, <количество>) - уменьшает запас items"""
        pass

    @abstractclassmethod
    def get_free_space(self):
        """вернуть количество свободных мест"""
        pass

    @abstractclassmethod
    def get_items(self):
        """возвращает сожержание склада в словаре {товар: количество}"""
        pass

    @abstractclassmethod
    def get_unique_items_count(self):
        """возвращает количество уникальных товаров"""
        pass


class Store(Storage):
    def __init__(self):
        self.items = {}
        self.capacity = 100

    def add(self, name, count):
        """(<название>, <количество>)  - увеличивает запас items с учетом лимита capacity"""
        if self.get_free_space() > 0:
            if self.get_free_space() >= count:
                print(f'Товар {name} добавлен')
                if name in self.items.keys():
                    self.items[name] = self.items[name] + count
                else:
                    self.items[name] = count
                return True
            else:
                print(f'Не хватает места для хранения. Максимум - {self.get_free_space()}')
        else:
            print('Нет места!')
        return False

    def remove(self, name, count):
        """(<название>, <количество>) - уменьшает запас items но не ниже 0"""
        if name in self.items.keys():
            if self.items[name] >= count:
                print('Есть нужное количество')
                self.items[name] = self.items[name] - count
                return True
            else:
                print(f'Неверное количество товара. Максимум -  {self.get_free_space()}')
        else:
            print('Такого товара нет')
        return False

    def get_free_space(self):
        """вернуть количество свободных мест"""
        count = 0
        for item in self.items.values():
            count += item
        return self.capacity - count

    def get_items(self):
        """возвращает сожержание склада в словаре {товар: количество}"""
        return self.items

    def get_unique_items_count(self):
        """возвращает количество уникальных товаров"""
        return len(self.items.keys())


class Shop(Store):
    def __init__(self):
        self.items = {}
        self.capacity = 20
        self.unique_count = 5

    def add(self, name, count):
        """(<название>, <количество>)  - увеличивает запас items с учетом лимита capacity"""
        if self.get_unique_items_count() + 1 <= self.unique_count:
            super().add(name, count)
            return True
        else:
            print(f'Не хватает места для хранения. В Shop хранится не больше {self.unique_count} разных товаров')
            return False


class Request:
    def __init__(self, str_input):
        data = str_input.split(' ')
        self.from_ = data[4]
        self.to = data[6]
        self.amount = int(data[1])
        self.product = data[2]

    def __repr__(self):
        return f'Доставить {self.amount} {self.product} из {self.from_} в {self.to}'






