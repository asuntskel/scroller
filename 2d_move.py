import os

size = 5
maps = {"blank" : [["_" for i in range(size)] for i in range(size)]}



class Char():
	def __init__(self, x, y, icon):
		self.x = x
		self.y = y
		self.lastx = 0
		self.lasty = 0
		self.icon = icon

	def getPosition(self):
		return (self.x, self.y)

	def move(self, key_direction):
		self.lastx = self.getPosition()[0]
		self.lasty = self.getPosition()[1]
		

		limit_value_inc = -1 if key_direction == "a" and self.x > 0 else 0
		self.x += limit_value_inc
		
		limit_value_inc = 1 if key_direction == "d" and self.x < size -1 else 0
		self.x += limit_value_inc

		if key_direction == "w":
			if self.y > 0:
				self.y -= 1
			else:
				self.y = self.y

		if key_direction == "s":
			if self.y < size-1:
				self.y += 1
			else:
				self.y = self.y




character = Char(3,3, "$")
enemy = Char(0,1, "Z")
entities = [character, enemy]
def refresh_console():
	return os.system('CLS')

def add_entities():
	# set the entities icons in the according coordinates
	# then print the whole grid with its entities

	for entity in entities:
		
		grid[entity.y][entity.x] = entity.icon
		print("DEBUG", entity.icon, entity.x, entity.y)
		#if entity.y != entity.lasty and entity.x != entity.lastx:
			#grid[entity.lasty][entity.lastx] = "*"

	for row in grid:
		print(row)
	return grid

grid = maps['blank']

while True:
	refresh_console()
	add_entities()
	character.move(input())








