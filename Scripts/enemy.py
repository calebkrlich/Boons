from enum import Enum

class BoonType(Enum):
    RED = 1
    BLUE = 2
    GREEN = 3

class Enemy:
    def __init__(self, enemyType, pathToFollow):
        self.type = enemyType
        self.movePath = pathToFollow
        self.currentMovePathIndex = 0
        self.image = None
        self.health = 1
        self.pos = (0,0)

    def move(self, pos):
        self.currentMovePathIndex += 1
        self.pos = self.movePath[self.currentMovePathIndex]
    
    def getHealth(self):
        return self.health
    
    def damage(self, amount):
        self.health -= amount

