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

    delay = 0.5   # Delay between each step

    def __init__(self, gameSize=10, initialLength=3):
        assert gameSize > 2*initialLength
        self.size = gameSize
        self.length = initialLength
        start = Point(random.randint(initialLength, gameSize-initialLength), random.randint(initialLength, gameSize-initialLength))
        self.body = deque([Point(start.x + i, start.y) for i in range(initialLength)])
        self.bites = deque([])
        assert self.putFood() != None

    def move(self, direction):
        prospect = onward[direction](self.body[0])
        if prospect.x < 0 or prospect.y < 0 or prospect.x >= self.size or prospect.y >= self.size or prospect in self.body:
            return None
        else:
            if prospect == self.food:
                if self.putFood() == None:
                    return None
                else:
                    self.bites.append(prospect)
            if len(self.bites) > 0 and self.body[len(self.body)-1] == self.bites[0]:
                self.bites.popleft()
            else:
                self.body.pop()
            self.body.appendleft(prospect)
            return self.body[0]

    def putFood(self):
        if (self.length > ((self.size*self.size) - 5)):
            return None
        else:
            while True:
                prospect = Point(random.randint(0, self.size-1), random.randint(0, self.size-1))
                if prospect not in self.body:
                    self.food = prospect
                    return self.food

    def draw(self):
        grid = [['.' for x in range(self.size)] for x in range(self.size)]
        for i, p in enumerate(self.body):
            grid[p.y][p.x] = str(i+1)
        for p in self.bites:
            grid[p.y][p.x] = 'o'
        grid[self.food.y][self.food.x] = 'y'
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
Snake(27, 5).run([Direction(random.randint(1, 4)) for i in range(30)])
