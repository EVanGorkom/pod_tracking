from enum import Enum

class Color(Enum):
    W = 'White'
    U = 'Blue'
    B = 'Black'
    R = 'Red'
    G = 'Green'
    C = 'Colorless'

    @classmethod
    def choices(cls):
        return [(key.value, key.name) for key in cls]