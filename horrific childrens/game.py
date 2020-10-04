import os

class Game():
    def __init__(self, size, entityList):
        self.size = size
        self.entityList = entityList
        self.map = [[" " for i in range(size)] for i in range(size)]

    def refresh(self):
        self.map = [[" " for i in range(self.size)] for i in range(self.size)]
    def printmap(self):
        for row in self.map:
            print(row)


class newEntity():
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def move(self, destination, refreshfunction, grid):
        self.destination = destination
        if destination == "a":
            refreshfunction()
            if entity.x == 0:
                entity.x = entity.x
            else:
                entity.x -= 1

        elif destination == "d":
            refreshfunction()
            print(grid.size)
            if entity.x != grid.size-1:
                entity.x += 1
            else:
                entity.x = entity.x
        
        if destination == "w":
            refreshfunction()
            if entity.y == 0:
                entity.y = entity.y
            else:
                entity.y -= 1

        elif destination == "s":
            refreshfunction()
            print(grid.size)
            if entity.y != grid.size-1:
                entity.y += 1
            else:
                entity.y = entity.y
        

def cls():
    os.system("CLS")

entities = []
newCharacter = newEntity(5, 5)
entities.append(newCharacter)
gamegrid = Game(size=10, entityList = entities)

# initial refresh

cls() # clear screen
gamegrid.refresh() # first refresh of the map
for entity in entities: # check entityList to add symbols to each coordinate
    gamegrid.map[entity.y][entity.x] = "E"
gamegrid.printmap()



#gameloop
while True:
    for entity in entities:
        direction = input("Move? WASD + enter to move.") # ask direction
        entity.move(direction, gamegrid.refresh, gamegrid) # move to direction and refresh old map (list)
        gamegrid.map[entity.y][entity.x] = "E"
        cls()
    gamegrid.printmap()
