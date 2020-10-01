import os

size = 20
grid = [["_" for i in range(size)] for i in range(size)]

class Char():
	def __init__(self, x, y, icon):
		self.x = x
		self.y = y
		self.lastx = 0
		self.lasty = 0
		self.icon = icon

	def getPosition(self):
		return (self.x, self.y)

	def move(self, direction):
		self.lastx = self.getPosition()[0]
		self.lasty = self.getPosition()[1]
		if direction == "a":
			self.x -= 1
		elif direction == "d":
			self.x += 1
		elif direction == "w":
			self.y -= 1
		elif direction == "s":
			self.y += 1

def keyInput(input):
	
	if input == "a":
		self.move(nextx-1, self.lastx)



character = Char(1,5, "O")
enemy = Char(0,8, "W")
entities = [character, enemy]

def build_map(tilemap):
	for entity in entities:
		grid[entity.y][entity.x] = entity.icon

		if grid[entity.lasty][entity.lastx] != "_":
			grid[entity.lasty][entity.lastx] = "_"

	for row in tilemap:
		print(row)

while True:
	os.system('CLS')
	for entity in entities:
		print(entity.x, entity.y)
	build_map(grid)
	
	character.move(input())





