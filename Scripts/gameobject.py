class GameObject():
    def __init__(self, image, startPos):
        self.image = image
        self.pos = startPos

    def move(self, position):
        self.pos = position
