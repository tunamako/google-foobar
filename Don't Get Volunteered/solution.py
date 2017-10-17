#I'm glad breadth-first searches exist or i'd be in a heap of trouble trying to get to and from my bunk!
import math
import 	Queue

class Tile():
	def __init__(self, board, x = 0, y = 0):
		self.board, self.x, self.y = board, x, y
		self.checked = False
		self.distance = 0

	def matches(self, aTile):
		return aTile.x == self.x and aTile.y == self.y
		
	def getNeighbors(self):
		xMoves = [-2, -2, -1, -1, 1, 1, 2, 2]
		yMoves = [-1, 1, -2, 2, -2, 2, -1, 1]
		neighbors = []
		for i in range(8):
			tileX = self.x + xMoves[i]
			tileY = self.y +  yMoves[i]
			if(self.board.isValidTile(tileX, tileY)):
				neighbors.append(self.board.getTileAt(tileX, tileY))
		return neighbors

class Board():
	def __init__(self, size):
		self.size = size
		self.grid = [[Tile(self, y, x) for x in range(self.size)] for y in range(self.size)]

	def getTileAt(self, x, y, n=-1):
		if n == -1:
			return self.grid[x][y]
		else:
			x = int(math.floor(n/self.size))
			y = int(n %self.size)
			return self.grid[x][y]

	def isValidTile(self, x, y):
		return x < self.size and y < self.size and x >= 0 and y >= 0

def answer(src, dest):
	gameBoard = Board(8)

	#Convert inputs to xy-coordinates and put in a tile object for easier handling
	srcTile = gameBoard.getTileAt(None, None, src)
	destTile = gameBoard.getTileAt(None, None, dest)

	#A queue will keep track of the tiles whose neighbors need to be looked at, starting with src
	checkQueue = Queue.Queue(maxsize = 0)
	checkQueue.put(srcTile)

	while(not checkQueue.empty()):
		tile = checkQueue.get()
		depth = tile.distance
			
		if tile.matches(destTile):
			return depth

		if(not tile.checked):
			tile.checked = True
			for i in tile.getNeighbors():
				i.distance = depth + 1
				checkQueue.put(i)
	return -1