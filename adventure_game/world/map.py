"""

"""
import random
from typing import List

from world.room import Foyer, Overlook, Narrow, Room, Treasure

_valid_difficulties: List[str] = ['easy', 'medium', 'hard']
_available_rooms: List[Room] = [Foyer, Narrow, Overlook, Treasure]


class MapError(Exception):
    """Invalid parameters given for map configuration"""


def _validate_gridspace(width: int, length: int) -> None:
    """Ensure given map size is valid"""
    if (width < 1) | (length < 1):
        raise MapError("Map dimensions must be positive values")


class Grid(object):
    """
    """
    layout: List[Room] = []

    def __init__(self, n_cols: int, n_rows: int) -> None:
        choices = list(range(0, len(_available_rooms)))
        for col in range(n_cols):
            tmp = []
            for row in range(n_rows):
                choice = random.choice(choices)
                tmp.append(_available_rooms[choice])
                choices.remove(choice)
            self.layout.append(tmp)

    def __call__(self):
        return self.layout


class WorldMap(object):
    """
    """

    def __init__(self, size: List[int], difficulty: str):
        # Ensure valid dimensionality of world map
        print("Loading...")
        if len(size) > 2:
            raise MapError("`size` argument must be format [width,length]")
        _validate_gridspace(size[0], size[1])
        print("Generating world map...")
        self._grid = Grid(n_cols=size[0], n_rows=size[1])
        # Validate difficulty argument, and assign.
        if difficulty not in _valid_difficulties:
            raise MapError(
                f"'{difficulty}' invalid option for difficulty setting"
            )
        self._difficulty = difficulty

    @property
    def layout(self):
        return [[room.name for room in vector] for vector in self._grid()]


test = WorldMap(size=[2, 2], difficulty="easy")
print(test.layout)
