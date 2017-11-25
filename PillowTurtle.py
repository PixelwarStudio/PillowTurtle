from math import cos, sin, radians as rad
from PIL import ImageDraw
import attr

@attr.s
class Turtle(object):
    pos = attr.ib(default=[0, 0])
    rot = attr.ib(default=0)
    visible = attr.ib(default=True)
    width = attr.ib(default=1)
    color = attr.ib(default=(255, 255, 255))

    def __attrs_post_init__(self):
        self._path = [] 
        self._stack = []

    def move(self, dist):
        if self.visible:
            if self._path == [] or self._path[len(self._path)-1] is False:
                self._path.append([(self.x, self.y)])
        else:
            self._path.append(False)
                
        # Calculate new position
        rad_rot = rad(self.rot)
        self.x += cos(rad_rot) * dist
        self.y += sin(rad_rot) * dist

        if self.visible:
            self._path.append([(self.x, self.y), self.width, self.color])

    def rotate(self, degrees):
        self.rot += degrees
    
    def push(self):
        self._stack.append((self.x, self.y))
        self._stack.append(self.rot)

    def pop(self):
        prev_visible = self.visible

        self.visible = False

        self.rot = self._stack.pop()
        self.pos = self._stack.pop()

        self.visible = prev_visible
    
    def draw(self, canvas):
        draw = ImageDraw.Draw(canvas)
        for n in range(1, len(self._path)):
            if self._path[n] is False or self._path[n-1] is False:
                continue

            p1, p2 = self._path[n-1][0], self._path[n][0]
            color, width = self._path[n][2], self._path[n][1]

            draw.line(p1+p2, color, width)

    @property
    def x(self):
        return self.pos[0]

    @x.setter
    def x(self, x):
        self.pos[0] = x

    @property
    def y(self):
        return self.pos[1]

    @y.setter
    def y(self, y):
        self.pos[1] = y

