import pytest
from random import randint, seed

from turtle import Turtle
from PillowTurtle import Turtle as Turtle2

seed(23423)

def init_turtles():
    t1 = Turtle()
    t1.speed(0)
    t2 = Turtle2([0, 0])

    return (t1, t2)

testdata_forward = [(randint(0, 300)) for i in range(50)]
@pytest.mark.parametrize("dist", testdata_forward)
def test_forward(dist):
    turtles = init_turtles()

    for turtle in turtles:
        turtle.forward(dist)
    
    assert turtles[0].pos() == pytest.approx(tuple(turtles[1].pos), 0.01)

def test_move_forward_backward():
    t1 = Turtle2([0,0])
    t2 = Turtle2([0,0])
    t3 = Turtle2([0,0])

    t1.forward(100)
    t2.move(100)
    t3.backward(-100)

    assert t1.pos == t2.pos == t3.pos

testdata_rotation = [(randint(0, 360), randint(0, 300)) for i in range(50)]
@pytest.mark.parametrize("angle, dist", testdata_rotation)
def test_rotation(angle, dist):
    turtles = init_turtles()

    for turtle in turtles:
        turtle.right(angle)
        turtle.forward(dist)
    
    assert turtles[0].pos() == pytest.approx(tuple(turtles[1].pos), 0.01)

def test_rotate_left_right():
    t1 = Turtle2([0,0])
    t2 = Turtle2([0,0])
    t3 = Turtle2([0,0])

    t1.right(10)
    t2.left(-10)
    t3.rotate(-10)

    assert t1.rot == t2.rot == t3.rot

def test_random_walk():
    turtles = init_turtles()

    for i in range(50):
        if i % 2 == 0:
            angle = randint(0, 360)
            turtles[0].right(angle)
            turtles[1].right(angle)
        else:
            dist = randint(0, 30)
            turtles[0].forward(dist)
            turtles[1].forward(dist)
    
    assert turtles[0].pos() == pytest.approx(tuple(turtles[1].pos), 0.01)
