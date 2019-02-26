import ElephantPop
import Disasters
import Math

#Monthly Updates
class ElephantReserve:
	def __init__(self, name = "Elephant Reserve"):	
		#Static Factors
		self.name			=	name
		self.mapSize		=	random.randint(1, 10)		#size of environment
		self.map			=	[]							#list of provinces in map, len(map) = size
		
		for province in range(self.mapSize):
			province		=	Biomes.Biome()
			province.name	=	str(province.type) + " Province " + str(self.num)
			
			self.map.append(province)	
		
		self.carryingCap	=	random.randint(1000, 10000)*biome.popMod*biome.tempMod 	#default carrying capacity of environment
		
		#Time Tracking
		self.month			=	0
		self.year			=	0
	
	def update(self):
		if self.month < 12:
			self.month += 1
		else:
			self.month = 0
			self.year += 1
		
	def (self):
		
	
	def disaster(self):
		a	=	0
	