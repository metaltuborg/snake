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

rewind = {
    Direction.WEST: eastOf,
    Direction.EAST: westOf,
    Direction.NORTH: southOf,
    Direction.SOUTH: northOf
}

onward = {
    Direction.WEST: westOf,
    Direction.EAST: eastOf,
    Direction.NORTH: northOf,
    Direction.SOUTH: southOf
}

def trace(start: Point, moves):
    loc, tail = start, deque([])
    for m in moves:
        loc = rewind[m](loc)
        tail.append(loc)
    return tail


class Snake:

    delay = 0.35   # Delay between each step

    def __init__(self, gameSize=10, initialLength=3):
        assert gameSize > 2*initialLength
        self.size = gameSize
        self.length = initialLength
        self.head = Point(x=random.randint(initialLength, gameSize-initialLength), y=random.randint(initialLength, gameSize-initialLength))
        self.moves = deque([Direction.WEST for x in range(initialLength-1)])
        self.tail = trace(self.head, self.moves)

    def move(self, direction):
        prospect = onward[direction](self.head)
        if prospect.x < 0 or prospect.y < 0 or prospect.x >= self.size or prospect.y >= self.size or prospect in self.tail:
            return None
        else:
            self.tail.appendleft(self.head)
            self.tail.pop()
            self.head = prospect
            self.moves.appendleft(direction)
            self.moves.pop()
            # self.tail = trace(self.head, self.moves)
            return self.head

    def draw(self):
        grid = [['.' for x in range(self.size)] for x in range(self.size)]
        grid[self.head.y][self.head.x] = 'o' # str(1)
        for i, p in enumerate(self.tail):
            grid[p.y][p.x] = 'x' # str(i+2)
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


# Snake(15, 4).run([Direction.WEST, Direction.WEST, Direction.NORTH, Direction.WEST])
Snake(27, 9).run([Direction(random.randint(1, 2)) for i in range(30)])
