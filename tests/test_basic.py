import pytest
from random import randint

from turtle import Turtle
from PillowTurtle import Turtle as Turtle2

def init_turtles():
    t1 = Turtle()
    t1.speed(0)
    t2 = Turtle2()
    t2.pos = [0, 0]

    return (t1, t2)

testdata_rotation = [(randint(0, 360), randint(0, 300)) for i in range(100)]

@pytest.mark.parametrize("angle, dist", testdata_rotation)
def test_rotation(angle, dist):
    turtles = init_turtles()

    for turtle in turtles:
        turtle.right(angle)
        turtle.forward(dist)
    
    assert turtles[0].pos() == pytest.approx(tuple(turtles[1].pos), 0.01)
