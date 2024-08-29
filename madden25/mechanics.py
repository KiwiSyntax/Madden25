import random

"""
This is the Compx class. This is the enemy computer. Most logic involving the computer will be here.
"""
class Compx:
	def __init__(self, window_x, window_y): # This is a constructor that initializes the object
		self.compxx = random.randint(0,1) # This was your original compx, I didn't know what else to call it
		self.position = [random.randrange(1, (window_x//10)) * 10, random.randrange(1, (window_y//10)) * 10] #setting the position using values given by window_x and window_y
		self.body = [random.randrange(1, (window_x//10)) * 10, random.randrange(1, (window_y//10)) * 10]
		self.direction = 'RIGHT'

	#Method to return Compxx value created. This will return an integer of 1 or 0
	def getCompxx(self):
		return self.compxx

	#Get the direction of the computer enemy in a STRING value
	def getDirection(self):
		return self.direction
	
	#Method to return a value in the list with the specified index.
	def getPosition(self, index):
		try:
			return self.position[index]
		except:
			return "Index out of range"

	#This returns the entire list of the body .
	def getBodyList(self):
		return self.body
	
	#Method to return value of list in index specified 
	def getBody(self, index):
		try:
			return self.body[index]
		except:
			return "Index out of range"

	#Change the integer value of compxx
	def changeCompxx(self, newValue):
		self.compxx = newValue

	#Swap out the current list with a new one for position
	def changePositionList(self, newList):
		self.position = newList

	#Method to change Position value given the new value and index
	def changePosition(self, index, newPosition):
		self.position[index] = self.position[newPosition] #index is where you want to put it and newPosition is the actual value
		#self.checkCollision()

	#This is supposed to move the computer enemy towards the player. You need the player object and yardline because I don't know why you use it
	def chasePlayer(self, playero, yardline):
		if self.position[0] > playero.getPosition(0):
			if yardline < 50:
				self.position[0] -= random.randint(5,8)
			else:
				self.position[0] -= random.randint(7,10)
			self.direction = 'LEFT'
		if self.position[0] < playero.getPosition(0):
			if yardline < 50:
				self.position[0] += random.randint(5,8)
			else:
				self.position[0] += random.randint(7,10)
			self.direction = 'RIGHT'
		if self.position[1] > playero.getPosition(1):
			if yardline < 50:
				self.position[1] -= random.randint(5,8)
			else:
				self.position[1] -= random.randint(7,10)
		if self.position[1] < playero.getPosition(1):
			if yardline < 50:
				self.position[1] += random.randint(5,8)
			else:
				self.position[1] += random.randint(7,10)

#You can use this object to keep a counter but you can also just use a global variable tbh
class DownCounter:
	def __init__(self):
		self.counter = 0

	def increaseCounter(self):
		self.counter = self.counter + 1
	
	def returnCounter(self):
		return self.counter


"""
This is the player class. You can use it to modify anything involving the player.
"""
class Playero:
	def __init__(self):
		self.direction = 'RIGHT'
		self.position = [0,250]
		self.body = [[0,250]]

		#This will return the direction as a STRING
	def getDirection(self):
		return self.direction
	
		#This will return the entire list in position
	def getPositionList(self):
		return self.position
	
		#This will return the entire list in body
	def getBodyList(self):
		return self.body
	
		#This will get the position of the list with the specified index and return the value
	def getPosition(self, index):
		try:
			return self.position[index]
		except:
			return "Index out of range"
		
		#This will change the STRING direction with the new STRING direction provided
	def changeDirection(self, newDirection):
		self.direction = newDirection
	
		#This will insert whatever you want in newPosition into the body list and then .pop()
		#I also don't know why you did this but I just rewrote it.
	def changeBody(self, index, newPosition):
		self.body.insert(index, newPosition)
		self.body.pop()

		#This will change the value of the current position list at the given index with the new value
	def changePosition(self, index, newPosition):
		self.position[index] = newPosition
	
		#Method to check collision returns 1 if there is collision and 0 if there is none
	def checkCollision(self, compx):
		if self.position[0] == compx.getPosition(0) and self.position[1] == compx.getPosition(1):
			return 1
		else:
			return 0

