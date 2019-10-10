
from unittest import TestCase

from ObjectBucket.ObjectBucket import ObjectBucket


class Fuu:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__counter: int = 0
        pass

    def set_counter(self, value: int):
        self.__counter = value
        pass

    def get_counter(self) -> int:
        return self.__counter
        pass


class TestObjectBucket(TestCase):

    def test_add_and_get(self):
        bucket = ObjectBucket()

        fuu = Fuu()
        fuu.set_counter(41)

        bucket.add("Fuu", Fuu, fuu)
        bucket.get("Fuu", Fuu).set_counter(23)

        assert bucket.get("Fuu", Fuu).get_counter() is 23
        pass

    pass
