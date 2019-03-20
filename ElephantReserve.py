import ElephantPop
import Biomes
import math
import random
#import Disasters

#Monthly Updates
class ElephantReserve:
	def __init__(self, name = "Elephant Reserve", mapSize = random.randint(1, 12)):	
		#Static Factors
		self.name			=	name
		self.mapSize		=	mapSize			#size of environment
		self.map			=	[]				#list of 2-lists, provinces in map, len(map) = size, entries are in format [province, provPop]
		
		#Time Tracking		
		self.month			=	0				#Current simulation month (of year)
		self.monthTot		=	0				#Current simulation month (total # of months since start)
		self.year			=	0				#Current simulation year
		
		#Total Reserve Tracking Info
		self.reserveCarryingCap	=	0
		self.reservePopulation	=	0
		
		#Time Tracking
		self.month			=	0
		self.year			=	0
		self.monthTot		=	0
		
		#Trackers for keeping track of which province and population we are on
		self.provNum = 0					#Numerical value of next province
		self.popNum	= 0						#Numerical value of next pop group
		self.elephantNum = 0				#Numerical value of next elephant
		
		#Province/Biom & Population Generation:
		for province in range(self.mapSize):
			#Create Biome/Province:
			#(Provinces are made up of biomes)
			newProv				=	Biomes.Biome("Unnamed", "Indeterminate", random.randint(1, 10), self.month)
			newProv.provNum		=	self.provNum
			newProv.name		=	"Province #%d - (%s)" % (newProv.provNum, newProv.type)
			newProv.id			=	newProv.idLabel + "[n]" + str(self.provNum)	
			self.provNum += 1
			
			#Create pop in biome/Province
			newPop = ElephantPop.ElephantPop(newProv.id, self.popNum, newProv.carryingCap, self.month, self.monthTot, self.elephantNum, popInit = 100)
			self.popNum	+=	1
			
			self.map.append([newProv, newPop])
			
			self.reserveCarryingCap	+=	newProv.carryingCap
			self.reservePopulation 	+=	newPop.population
		
	def updateReserve(self):
		self.monthTot += 1
		if self.month < 12:
			self.month += 1
		else:
			self.month = 0
			self.year += 1
		
		for province in self.map:
			#province[0].updateBiome()
			province[1].updatePop()
		
	#def migration(self, oldProvince, newProvince):
		