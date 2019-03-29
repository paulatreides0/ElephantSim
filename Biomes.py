import math
import random

#Biomes serve as environmental subsections as well as provinces
class Biome:
	def __init__(self, name, type, size, month):
		#Biome reference information
		self.name		=	name						#name only has fluff purposes
		self.type		=	type						#string-type, name of biome type
		self.idLabel	=	"00xInd"					#Used to dynamically generate names
		self.provNum	=	0							#Another name of province, references it as a number, e.g. "Province 1"
		self.id			=	0							#Identification code of province, used as defacto name, idlabel + provnNum e.g. 00xInd[n]01
	
		#Stores & Governs connections between biomes
		self.noLink		=	[]							#List-type, which biomes the biome cannot be directly next to - uses idLabels as list elements
		self.linkCap	=	4							#Limit on number of connections between provinces, defaults to 4
		self.linkMap	=	[]							#List-type, documents which other biomes this biome is connected to as Biome-objects
	
		#Handles primary biome mods - temperature, water, and size
		self.temp		=	random.randint(0, 2)		#temperature, -5 to 5 scale, 0 is default, 2 to 3 is ideal, -5 is instant total death, 4+ is too hot
		self.water		=	random.randint(0, 2)		#environmental water supply, -5 to 5 scale, 0 is default, 2 to 3 is ideal, -5 is instant total death, 4+ is flooding
		self.size		=	size						#size of biome, from 1 (tiny) to 10 (gigantic)
		
		#Special Features - Can modify individual biomes
		self.features	=	[]							#list-type, containing special features of biome
		self.featsMod	=	0
		for feature in self.features:
			self.featsMod += features[feature].popMod
		
		#tempMod defines temperature modifier on popCap
		tempFactor1			=	-0.15			#Temp factor when temp -5 < temp < 0
		tempFactor2			=	0.00			#Temp factor when 0 <= temp < 2 & 3 <= temp < 4
		tempFactor3			=	0.05			#Temp factor when 2 <= temp < 3
		tempFactor4			=	0.05			#Temp factor when temp >= 4
		if self.temp == -5:
			self.tempMod	=	0
		elif -5 < self.temp < 0:
			self.tempMod	=	1+(tempFactor1*self.temp)
		elif 0 <= self.temp < 2:
			self.tempMod	=	1+(tempFactor2*self.temp)
		elif 2 <= self.temp < 3:
			self.tempMod	=	1+(tempFactor2*self.temp)
		elif 3 <= self.temp < 4:
			self.tempMod	=	1+(tempFactor2*self.temp)
		else:
			self.tempMod	=	1+(tempFactor2*(2 - self.temp))
		
		#waterMod defines humidity modifier on popCap
		waterFactor1			=	-0.20			#Water factor when water -5 < water < 0
		waterFactor2			=	0.00			#Water factor when 0 <= water < 2 & 3 <= temp < 4
		waterFactor3			=	0.075			#Water factor when 2 <= water < 3
		waterFactor4			=	0.10			#Water factor when water >= 4
		if self.water == -5:
			self.waterMod	=	0
		elif -5 < self.water < 0:
			self.waterMod	=	1+(waterFactor1*self.water)
		elif 0 <= self.water < 2:
			self.waterMod	=	1+(waterFactor2*self.water)
		elif 2 <= self.water < 3:
			self.waterMod	=	1+(waterFactor2*self.water)
		elif 3 <= self.water < 4:
			self.waterMod	=	1+(waterFactor2*self.water)
		else:
			self.waterMod	=	1+(waterFactor2*(2 - self.water))
			
		#***RETURN TO LATER***
		##Disaster Module - Determines how disasters affect elephant pop
		self.disastersMod	=	1					#Temporary Value, will change when module properly introduced

		#***RETURN TO LATER***
		##Predation Module - Determines how predators behave & affect elephant pop.
		#self.predators		=	min(random.choice(0, random.randint(5, 50)),  elephantPop.population)
		#self.letahlity		=	random.randint(0, 1000000)*0.0000001
		#self.predatorCap	=	0
		self.predationMod	=	1					#Temporary Value, will change when module properly introduced
		
		#Initial carrying capacity of biome, can change with events & disasters
		self.biomePopMod = 0							
		for sizeFactor in range(self.size):
			self.biomePopMod += random.randint(500,1000)
			
		self.carryingCap	=	self.biomePopMod*self.waterMod*self.tempMod*self.featsMod*self.disastersMod*self.predationMod
	
	def updateCarryCap(self):
		self.carryingCap	=	self.biomePopMod*self.waterMod*self.tempMod*self.featsMod
		
	def updateSizeMod(self, newSize):
		self.size	+=	newSize
		self.updateCarryCap()
	
	def updateTempMod(self):
		if self.temp < 0:
			self.tempMod	=	1+(tempFactor1*self.temp)
		elif 0 <= self.temp <= 3:
			self.tempMod	=	1+(tempFactor2*self.temp)
		else:
			self.tempMod	=	1+(tempFactor2*(2 - self.temp))
		self.updateCarryCap()
			
	def updateWaterMod(self):
		if self.water < 0:
			self.waterMod	=	1+(waterFactor1*self.water)
		elif 0 <= self.water <= 3:
			self.waterMod	=	1+(waterFactor2*self.water)
		else:
			self.waterMod	=	1+(waterFactor2*(2 - self.water))
		self.updateCarryCap()
		
	def rename(self, newName):
		self.name = str(newName)
			
	def rainyMonth(self):
		self.water += 1
		self.updateWaterMod()
			
	def torrentialRain(self):
		self.water += 2
		self.updateWaterMod()
		
	def typhoonRain(self):
		self.water += 3
		self.updateWaterMod()
		
	def dryMonth(self):
		self.water -= 1
		self.updateWaterMod()
	
	def aridMonth(self):
		self.water -= 2
		self.temp += 1
		self.updateTempMod()
		self.updateWaterMod()
		
	def hotMonth(self):
		self.temp += 1
		self.updateTempMod()
		
	def heatWave(self):
		self.temp += 2
		self.updateTempMod()
		
	def coldSnap(self):
		self.temp -= 1
		self.updateTempMod()
		
	def arcticFront(self):
		self.temp -= 2
		self.updateTempMod()
		
	#def updateBiome(self):
		#Method for dynamically changing biome and biomerestrictions over time
		
	#def Terraform(self, featureRemove = [], featureAdd = [])
	#	for feature in featureRemove:
	#		if 
	#	for feature in featureAdd:
	#		if feature

class Arctic(Biome):
	def __init__(self):
		Biome.__init__(type = "Arctice", size = random.randint(1, 10))
		
		self.idlabel 	=	"01xArtc"
		self.noLink		=	["04xRnft", "06xWtln","08xDsrt", "09xSvnh", "10xGsln", "12xChpl"]
	
class Tundra(Biome):
	def __init__(self):
		Biome.__init__(type = "Tundra", size = random.randint(1, 10))
		
		self.idlabel	=	"02xTndr"
		self.noLink		=	["04xRnft"]
		
class Forest(Biome):
	def __init__(self):
		Biome.__init__(type = "Forest", size = random.randint(1, 10))
		
		self.idlabel	=	"03xFrst"
		self.noLink		=	[]

class Rainforest(Biome):
	def __init__(self):
		Biome.__init__(type = "Rainforest", size = random.randint(1, 10))
		
		self.idlabel	=	"04xRnft"
		self.noLink		=	["01xArtc", "02xTndr", "08xDsrt", "11xTaig"]

class Mountains(Biome):
	def __init__(self):
		Biome.__init__(type = "Mountains", size = random.randint(1, 10))
		
		self.idlabel	=	"05xMtns"
		self.noLink		=	[]

class Wetlands(Biome):
	def __init__(self):
		Biome.__init__(type = "Wetlands", size = random.randint(1, 10))

		self.idlabel	=	"06xWtln"
		self.noLink		=	["01xArtc", "08xDsrt"]
		
class Drylands(Biome):
	def __init__(self):
		Biome.__init__(type = "Drylands", size = random.randint(1, 10))

		self.idlabel	=	"07xDrln"
		self.noLink		=	[]
		
class Desert(Biome):
	def __init__(self):
		Biome.__init__(type = "Desert", size = random.randint(1, 10))

		self.idlabel	=	"08xDsrt"
		self.noLink		=	["01xArtc", "04xRnft", "06xWtln", "09xSvnh", "11xTaig", "12xChpl"]
		
class Savannah(Biome):
	def __init__(self):
		Biome.__init__(type = "Savannah", size = random.randint(1, 10))
		
		self.idlabel	=	"09xSvnh"
		self.noLink		=	["01xArtc", "08xDsrt"]
		
class Grasslands(Biome):

	def __init__(self):
		Biome.__init__(type = "Grasslands", size = random.randint(1, 10))
		
		self.idlabel	=	"10xGsln"
		self.noLink		=	["01xArtc", "08xDsrt"]
		
class Taiga(Biome):

	def __init__(self):
		Biome.__init__(type = "Taiga", size = random.randint(1, 10))
		
		self.idlabel	=	"11xTaig"
		self.noLink		=	["04xRnft", "08xDsrt"]
		
class Chapparal(Biome):
	def __init__(self):
		Biome.__init__(type = "Chapparal", size = random.randint(1, 10))
		
		self.idlabel	=	"12xChpl"
		self.noLink		=	["01xArtc", "08xDsrt"]
		
