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

		#Tracks matings, pregnancies, and births
		self.pregList	=	[]
		self.births		=	0
		
		#Populates initial elephant pop
		for elephant in range(popInit):
			if initPop == True:
				newElephant = Elephant.Elephant(elephantNum, biomeId, month, monthTot)
				newElephant.elephantNum = elephantNum			#elephantNum will be initialized at higher, may 
				self.popList.append(newElephant)
				if newElephant.sex == "m":
					self.mList.append(newElephant)
				else:
					self.fList.append(newElephant)
				elephantNum += 1
	
	def updatePop(self):
		for elephant in self.popList:
			elephant.updateElephant()