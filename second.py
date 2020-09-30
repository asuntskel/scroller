class Entry():
    def __init__(self, x, y, mark):
        self.x = x
        self.y = y
        self.mark = mark

    def update(self):
        grid[self.y][self.x] = self.mark



entities = []
grid = [["_" for i in range(3)] for i in range(3)]

def printmap(map):
    print(f"\n{grid[0]}\n{grid[1]}\n{grid[2]}\n")

def prompt():
    row = int(input("Row... "))
    col = int(input("Column... "))
    hit = str(input("X or O")).upper()
    return row, col, hit

def play():
    for entity in entities:
        entity.update()
    printmap(grid)

    while True:
        print("Target? (TOP to BOTTOM, LEFT TO RIGHT, TYPE)")
        entities.append(Entry(*prompt()))

        for entity in entities:
            entity.update()
        printmap(grid)
    else:
        quit()

play()


