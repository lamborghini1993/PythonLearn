import random
from typing import Union

from pydantic import BaseModel


class A(BaseModel):
    a: int
    s: str

    def __str__(self) -> str:
        return "A"


class B(BaseModel):
    b: int
    s: str

    def __str__(self) -> str:
        return "B"


class obj(BaseModel):
    x: Union[A, B]


def random_str():
    return "".join(random.choices("abcdefghijklmnopqrstuvwxyz", k=random.randint(1, 10)))


def random_a():
    return A(a=random.randint(1, 999), s=random_str())


def ramdom_b():
    return B(b=random.randint(1, 999), s=random_str())


def test():
    for _ in range(100):
        x = random_a() if random.randint(0, 1) else ramdom_b()
        o = obj(x=x)
        json = o.model_dump_json()
        xx = obj.model_validate_json(json)
        if xx.x != x:
            print(xx.x, x, json)


test()
