import math
import random

class Biome:
	def __init__(name = 0, type = 0, size = random.randint(1, 10)):
		self.name		=	name
		self.type		=	type						#string-type, name of biome type
		self.temp		=	random.randint(0, 2)		#temperature, -5 to 5 scale, 0 is default, 2 to 3 is ideal, -5 is instant total death, 4+ is too hot
		self.water		=	random.randint(0, 2)		#environmental water supply, -5 to 5 scale, 0 is default, 2 to 3 is ideal, -5 is instant total death, 4+ is flooding
		self.size		=	size						#size of biome, from 1 (tiny) to 10 (gigantic)
		
		self.features	=	[]							#list-type, containing special features of biome
		self.featsMod	=	0
		
		
		self.biomePopMod = 0							#Used to calculate base biome popCap based on size
		for sizeFactor in range(self.size):
			self.biomePopMod += random.randint(500,1000)
		
		for feature in self.features:
			self.featsMod += features[feature].popMod
		
		#tempMod defines temperature modifier on pop
		tempFactor1			=	-0.15			#Temp factor when temp -5 < temp < 0
		tempFactor2			=	0.00			#Temp factor when 0 <= temp < 2 & 3 <= temp < 4
		tempFactor3			=	0.05			#Temp factor when 2 <= temp < 3
		tempFactor4			=	0.05			#Temp factor when temp >= 4
		if self.temp == -5:
			self.tempMod	=	0
		elif -5 < self.temp < 0:
			self.tempMod	=	1+(tempFactor1*self.temp))
		elif 0 <= self.temp < 2:
			self.tempMod	=	1+(tempFactor2*self.temp))
		elif 2 <= self.temp < 3:
			self.tempMod	=	1+(tempFactor2*self.temp))
		elif 3 <= self.temp < 4:
			self.tempMod	=	1+(tempFactor2*self.temp))
		else:
			self.tempMod	=	1+(tempFactor2*(2 - self.temp))
		
		#waterMod defines humidity modifier on pop
		waterFactor1			=	-0.20			#Water factor when water -5 < water < 0
		waterFactor2			=	0.00			#Water factor when 0 <= water < 2 & 3 <= temp < 4
		waterFactor3			=	0.07			#Water factor when 2 <= water < 3
		waterFactor4			=	0.10			#Water factor when water >= 4
		if self.water == -5:
			self.waterMod	=	0
		elif -5 < self.water < 0:
			self.waterMod	=	1+(waterFactor1*self.water))
		elif 0 <= self.water < 2:
			self.waterMod	=	1+(waterFactor2*self.water))
		elif 2 <= self.water < 3:
			self.waterMod	=	1+(waterFactor2*self.water))
		elif 3 <= self.water < 4:
			self.waterMod	=	1+(waterFactor2*self.water))
		else:
			self.waterMod	=	1+(waterFactor2*(2 - self.water))
			
		#***RETURN TO LATER***
		#Disaster Module - Determines how disasters affect elephant pop
		self.disastersMod	=	1					#Temporary Value, will change when module properly introduced

		#***RETURN TO LATER***
		#Predation Module - Determines how predators behave & affect elephant pop.
		#self.predators		=	min(random.choice(0, random.randint(5, 50)),  elephantPop.population)
		#self.letahlity		=	random.randint(0, 1000000)*0.0000001
		#self.predatorCap	=	0
		self.predationMod	=	1					#Temporary Value, will change when module properly introduced
		
		#Initial carrying capacity of biome, can change with events & disasters
		self.carryingCap	=	self.biomePopMod*self.waterMod*self.tempMod*self.featsMod*self.disasterMod*self.predationMod
	
	def UpdateCarryCap(self):
		self.carryingCap	=	self.biomePopMod*self.waterMod*self.tempMod*self.featsMod
		
	def UpdateSizeMod(self, newSize):
		self.size	+=	newSize
		UpdateCarryCap()
	
	def UpdateTempMod(self):
		if self.temp < 0:
			self.tempMod	=	1+(tempFactor1*self.temp))
		elif 0 <= self.temp <= 3:
			self.tempMod	=	1+(tempFactor2*self.temp))
		else:
			self.tempMod	=	1+(tempFactor2*(2 - self.temp))
		
		UpdateCarryCap()
			
	def UpdateWaterMod(self):
		if self.water < 0:
			self.waterMod	=	1+(waterFactor1*self.water))
		elif 0 <= self.water <= 3:
			self.waterMod	=	1+(waterFactor2*self.water))
		else:
			self.waterMod	=	1+(waterFactor2*(2 - self.water))
	
		UpdateCarryCap()
		
	def Rename(self, newName):
		self.name = str(newName)
			
	def RainyMonth(self):
		self.water += 1
		UpdateWaterMod()
			
	def TorrentialRain(self):
		self.water += 2
		UpdateWaterMod()
		
	def HurricaneRain(self):
		self.water += 3
		UpdateWaterMod()
		
	def DryMonth(self):
		self.water -= 1
		UpdateWaterMod()
	
	def AridMonth(self):
		self.water -= 2
		self.temp += 1
		UpdateTempMod()
		UpdateWaterMod()
		
	def HotMonth(self):
		self.temp += 1
		UpdateTempMod()
		
	def HeatWave(self):
		self.temp += 2
		UpdateTempMod()
		
	def ColdSnap(self):
		self.temp -= 1
		UpdateTempMod()
		
	def ArcticFront(self):
		self.temp -= 2
		UpdateTempMod()
		
	#def Terraform(self, featureRemove = [], featureAdd = [])
	#	for feature in featureRemove:
	#		if 
	#	for feature in featureAdd:
	#		if feature

class Arctic(Biome):
	def __init__(self):
		Biome.__init__(type = "Arctice", size = random.randint(1, 10))
	
class Tundra(Biome):
	def __init__(self):
		Biome.__init__(type = "Tundra", size = random.randint(1, 10))
		
class Forest(Biome):
	def __init__(self):
		Biome.__init__(type = "Forest", size = random.randint(1, 10))

class Jungle(Biome):
	def __init__(self):
		Biome.__init__(type = "Jungle", size = random.randint(1, 10))

class Mountains(Biome):
	def __init__(self):
		Biome.__init__(type = "Mountains", size = random.randint(1, 10))

class Wetlands(Biome):
	def __init__(self):
		Biome.__init__(type = "Wetlands", size = random.randint(1, 10))
		
class Drylands(Biome):
	def __init__(self):
		Biome.__init__(type = "Drylands", size = random.randint(1, 10))

class Desert(Biome):
	def __init__(self):
		Biome.__init__(type = "Desert", size = random.randint(1, 10))

class Savannah(Biome):
	def __init__(self):
		Biome.__init__(type = "Savannah", size = random.randint(1, 10))