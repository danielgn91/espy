# src/espy/entity_set.py

from __future__ import annotations
from .ir import Operation, WhereOperation
from typing import TYPE_CHECKING, Generic, TypeVar

if TYPE_CHECKING:
    from .entity import Entity

T = TypeVar("T", bound="Entity")


class EntitySet(Generic[T]):
    """
    Representa uma consulta sobre um conjunto de entidades.

    Um EntitySet é imutável: cada operação retorna um novo EntitySet.
    """

    def __init__(
        self,
        entity_type: type[T],
        operations: list[Operation] | None = None,
    ):
        self.entity_type = entity_type
        self._operations = operations or []

    def __getattr__(self, name):

        methods = getattr(
            self.entity_type,
            "__espy_set_methods__",
            {},
        )

        if name in methods:

            def wrapper(*args, **kwargs):
                return methods[name](self, *args, **kwargs)

            return wrapper

        raise AttributeError(name)

    def where(self, **filters) -> "EntitySet[T]":
        return EntitySet(
            self.entity_type,
            operations=self._operations + [WhereOperation(filters)],
        )

    @property
    def operations(self):
        return tuple(self._operations)

    def __repr__(self):
        return (
            f"EntitySet("
            f"{self.entity_type.__name__}, "
            f"operations={self._operations})"
        )