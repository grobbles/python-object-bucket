from typing import TypeVar


class ObjectBucket:
    T = TypeVar('T')

    def __init__(self):
        self.__instance_bucket = {}
        self.__clazz_bucket = {}
        pass

    def add(self, name: str, clazz, instance):
        self.__instance_bucket[name] = instance
        self.__clazz_bucket[name] = clazz
        pass

    def get(self, key_name: str, key_clazz: T) -> T:
        if self.__clazz_bucket[key_name] is not key_clazz:
            raise KeyError()

        temp = self.__instance_bucket[key_name]
        return temp
        pass