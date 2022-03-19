from dataclasses import dataclass



@dataclass
class HexColor:
    def __init__(self, color="#FFFFFF"):
        if isinstance(color, str) and len(color) == 7 and color[0] == "#":
            if int(color[1:-1], 16):
                self.color = color
                return None
        raise Exception("Invalid Color")


@dataclass
class ColorPreset:
    bg_color: HexColor = "#FFFFFF"
    fg_color: HexColor = "#000000"


@dataclass
class Vector2:
    x: float = 0
    y: float = 0

    def __mul__(self, scalar):
        if isinstance(scalar, float) or isinstance(scalar, int):
            self.x *= scalar
            self.y *= scalar
            return Vector2(self.x, self.y)
        else:
            raise Exception("Tried to multiply Vector2 by a non scalar")

    def __add__(self, vector):
        if isinstance(vector, Vector2):
            self.x += vector.x
            self.y += vector.y
            return Vector2(self.x, self.y)
        else:
            raise Exception("Tried to add Vector2 by a non Vector2")

    def __sub__(self, vector):
        if isinstance(vector, Vector2):
            self.x -= vector.x
            self.y -= vector.y
            return Vector2(self.x, self.y)
        else:
            raise Exception("Tried to subtract Vector2 by a non Vector2")
