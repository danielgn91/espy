# src/espy/decorators.py

from __future__ import annotations

from collections.abc import Callable


def set_method(func: Callable) -> Callable:
    """
    Marca um método como pertencente ao EntitySet da entidade.
    """
    func.__espy_set_method__ = True
    return func


def singleton_method(func: Callable) -> Callable:
    """
    Marca um método como pertencente à entidade individual.
    """
    func.__espy_singleton_method__ = True
    return func