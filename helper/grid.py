from typing import Any
from collections.abc import Callable
from functools import cached_property
from typing import Generic, TypeVar


UP = complex(0, -1)
RIGHT = complex(1, 0)
DOWN = complex(0, 1)
LEFT = complex(-1, 0)

FOUR_DIRECTIONS = (UP, RIGHT, DOWN, LEFT)


TURN_LEFT = {UP: LEFT, RIGHT: UP, DOWN: RIGHT, LEFT: DOWN}
TURN_RIGHT = {UP: RIGHT, RIGHT: DOWN, DOWN: LEFT, LEFT: UP}

T = TypeVar('T')

class Grid(Generic[T]):
    def __init__(self, cells: dict[complex, T]):
        self._cells = cells

    @classmethod
    def from_str(cls, data: str, parse: Callable[[str], T] = None) -> 'Grid':
        cells = dict()
        for y, line in enumerate(data.splitlines()):
            for x, cell in enumerate(line):
                cells[complex(x, y)] = parse(cell) if parse else cell
        return cls(cells)

    @cached_property
    def width(self):
        return int(max(cell.real for cell in self._cells) + 1)
    
    @cached_property
    def height(self):
        return int(max(cell.imag for cell in self._cells) + 1)
    
    def __contains__(self, position: complex):
        return 0 <= position.real < self.width and 0 <= position.imag < self.height
    
    def __getitem__(self, position: complex) -> T:
        if position in self._cells:
            return self._cells[position]
        return None

    def __setitem__(self, position: complex, value: T):
        self._cells[position] = value
    
    @property
    def cells(self):
        return self._cells.items()