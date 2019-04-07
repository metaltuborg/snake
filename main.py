import random
import time
from enum import Enum
from collections import deque, namedtuple

Point = namedtuple('Point', ['x', 'y'])


class Direction(Enum):
    NORTH = 1
    WEST = 2
    SOUTH = 3
    EAST = 4

def northOf(p: Point) -> Point:
    return Point(p.x, p.y-1)

def southOf(p: Point) -> Point:
    return Point(p.x, p.y+1)

def eastOf(p: Point) -> Point:
    return Point(p.x+1, p.y)

def westOf(p: Point) -> Point:
    return Point(p.x-1, p.y)

onward = {
    Direction.WEST: westOf,
    Direction.EAST: eastOf,
    Direction.NORTH: northOf,
    Direction.SOUTH: southOf
}


class Snake:

    delay = 0.35   # Delay between each step

    def __init__(self, gameSize=10, initialLength=3):
        assert gameSize > 2*initialLength
        self.size = gameSize
        self.length = initialLength
        start = Point(x=random.randint(initialLength, gameSize-initialLength), y=random.randint(initialLength, gameSize-initialLength))
        self.body = deque([Point(start.x + i, start.y) for i in range(initialLength)])

    def move(self, direction):
        prospect = onward[direction](self.body[0])
        if prospect.x < 0 or prospect.y < 0 or prospect.x >= self.size or prospect.y >= self.size or prospect in self.body:
            return None
        else:
            self.body.appendleft(prospect)
            self.body.pop()
            return self.body[0]

    def draw(self):
        grid = [['.' for x in range(self.size)] for x in range(self.size)]
        for i, p in enumerate(self.body):
            grid[p.y][p.x] = str(i+1)
        print((self.size+2) * '-')
        for i in range(self.size):
            print('|' + ''.join(grid[i]) + '|')
        print((self.size+2) * '-')
    
    def run(self, steps):
        self.draw()
        for step in steps:
            time.sleep(self.delay)
            print('\n'*15, 'Going', str(step.name), '...', '\n'*3)
            if (self.move(step) == None):
                print("End of game!")
                break
            else:
                self.draw()


# Snake(27, 9).run([Direction.NORTH, Direction.NORTH, Direction.EAST, Direction.EAST, Direction.SOUTH, Direction.SOUTH])
Snake(27, 9).run([Direction(random.randint(1, 2)) for i in range(30)])
