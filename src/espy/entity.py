# src/espy/entity.py

from __future__ import annotations
from collections.abc import Callable
from typing import ClassVar
from .entity_set import EntitySet


class Entity:
    source: ClassVar[object | None] = None
    __espy_set_methods__: dict[str, Callable] = {}
    __espy_singleton_methods__: dict[str, Callable] = {}
    
    def __init__(self, id: int):
        self.id = id

    
    @classmethod
    def _register_methods(cls):

        cls.__espy_set_methods__ = {}
        cls.__espy_singleton_methods__ = {}

        for name, obj in vars(cls).items():

            if getattr(obj, "__espy_set_method__", False):
                cls.__espy_set_methods__[name] = obj

            if getattr(obj, "__espy_singleton_method__", False):
                cls.__espy_singleton_methods__[name] = obj
    
    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        cls._register_methods()


    @classmethod
    def all(cls) -> EntitySet:
        return EntitySet(cls)

    @classmethod
    def where(cls, **filters) -> EntitySet:
        return EntitySet(cls).where(**filters)