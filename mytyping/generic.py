from typing import Generic, TypeVar

T = TypeVar("T")


class A(Generic[T]):
    def __init__(self, t: T):
        self.t = t

    def get(self) -> T:
        return self.t

    def set(self, t: T):
        self.t = t


a = A(1)
print(a.get())
b = A[int](2)
print(b.get())
c = A[str]("3")
print(c.get())
