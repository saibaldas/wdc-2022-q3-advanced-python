#!/usr/bin/env python3

from typing import Union


def g(x: Union[) -> Any:
    return x * 2


def f(y: Any) -> Any:
    return g(y)


print(f(10))
print(f('a'))
