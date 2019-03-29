import Elephant
import random

class ElephantPop:
	def __init__(self, biomeId, popNum, popMax, month, monthTot, elephantNum, popInit = random.randint(100, 1000), initPop = True):
		self.popId		=	biomeId + str(popNum)  	#Equivalent of pop group "name"
		self.nomadLabel	=	False					#True if a nomadic (temporary) pop group
		self.initPop	=	initPop
		#Tracks population
		self.population	=	popInit
		self.popCap		=	popMax
		
		#Population Group Trackers
		self.popList	=	[]
		self.mList		=	[]
		self.fList		=	[]
		self.adultList	=	[[],[]]					#males in [0], females in[1]

		#Tracks matings, pregnancies, and births
		self.pregList	=	[]
		self.births		=	0
		
		#Populates initial elephant pop
		for elephant in range(popInit):
			if initPop == True:
				newElephant = Elephant.Elephant(elephantNum, biomeId, month, monthTot, initPop = True)
				newElephant.elephantNum = elephantNum			#elephantNum tracks the next elephant number up
				self.popList.append(newElephant)
				newElephant.associations.append(self.popList)
				if newElephant.sex == "m":
					self.mList.append(newElephant)
					newElephant.associations.append(self.mList)
					if newElephant.lifeStage == 3:
						self.adultList[0].append(newElephant)
						newElephant.associations.append(self.adultList)
				else:
					self.fList.append(newElephant)
					newElephant.associations.append(self.fList)
					if newElephant.lifeStage == 3:
						self.adultList[1].append(newElephant)
						newElephant.associations.append(self.adultList)
				
				elephantNum += 1
	
	def updatePop(self):
		for elephant in self.popList:
			elephantUpdate = elephant.updateElephant()
			#Incorporates new elephants into population
			
			#Checks if Elephant should be added/removed from adultList
			if elephantUpdate == True:
				if elephant.sex == "m":
					if elephant.lifeStage == 3:
						self.adultList[0].append(elephant)
						elephant.associations.append(self.adultList)
					elif elephant.lifeStage == 4:
						self.adultList[0].remove(elephant)
						elephant.associations.remove(self.adultList)
				else:
					if elephant.lifeStage == 3:
						self.adultList[1].append(elephant)
						elephant.associations.append(self.adultList)
					elif elephant.lifeStage == 4:
						self.adultList[1].remove(elephant)
						elephant.associations.remove(self.adultList)
			#Handles elephant mating
			if (elephant.fertility[0] == True) and (0 < elephant.fertility[1] <= 3):
				for instance in range(elephant.fertility[1]):
					if elephant.sex == "m":
						elephant.mate(random.choice(self.adultList[1]))
					else:
						elephant.mate(random.choice(self.adultList[0]))
			
			
			
			
			
			
			
			
			
			