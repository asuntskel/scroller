import os
def cls():
    os.system("CLS")

class Character():
    def __init__(self, x, y, symbol = "0"):
        self.x = x
        self.y = y
        self.nextx = x
        self.nexty = y
        self.symbol = symbol


    def move(self, inputDirection, MapObject):
        KEY_MAP = { # support for diagonals!
            "a": ["x", -1], 
            "d": ["x", 1], 
            "w": ["y", -1], 
            "s": ["y", 1]}
        
        chosen = inputDirection
        if KEY_MAP[chosen][0] == "x":
            self.x += KEY_MAP[chosen][1]
            print(self.x)
        elif KEY_MAP[chosen][0] == "y":
            self.y += KEY_MAP[chosen][1]
            print(self.y)
            

                
            #if self.x == KEY_MAP[key_input][0]:
            #self.x += KEY_MAP[key_input][1]
            #elif self.y == KEY_MAP[key_input][0]:
            #self.y += KEY_MAP[key_input][1]
class Map():
    def __init__(self, dimensions):
        self.dimensions = dimensions
        self.grid = [[" " for i in range(dimensions)] for i in range(dimensions)]

    def fullprint(self):
        for row in self.grid:
            print(row)
    
    def refresh(self):
        self.grid = [[" " for i in range(self.dimensions)] for i in range(self.dimensions)]
        
aMap = Map(5)
print(aMap.dimensions)
entities = [Character(3,3)]

def step():
    aMap.refresh() # restore the grid to its original (empty)
    for entity in entities: # loops thru the entities
        #print(entity.symbol, "--->", entity.x, entity.y) # show entities position in DEBUG
         
        aMap.grid[entity.y][entity.x] = entity.symbol
        #except IndexError:
            #entity.y -= 1
            #entity.x -= 1 # add entities symbols to their coordinates
    aMap.fullprint() #print the updated map
    aMap.checkCollision(entities[0].move(str(input()), aMap))


#a.fullprint() # initial print of the chosen map
cls()
while True:
    #cls()
    step()
