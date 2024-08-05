from enum import Enum


class GameType(Enum):
    CASUAL = 'casual'
    COMPETITIVE = 'competitive'

    def choices(cls):
        return [(key.value, key.name) for key in cls]