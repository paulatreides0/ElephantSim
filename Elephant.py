import math
import random

class Elephant:
	def __init__(self, elephantNum, biomeId, month, monthTot, initPop = False):
		#Static Factors & Tracking Information
		self.trackid		=	biomeId + "n" + str(elephantNum) 							#equivalent of name, native biomeId plus elephant number
		self.elephantNum	=	elephantNum + 1												#lists elephant #, simpler than trackid, current elephant number gets tracked at global level
		self.sex			=	random.choice(["m", "f"])									#"f" for female, "m" for male
		self.birthDay		=	[monthTot%12 + 1, math.floor(monthTot/12), monthTot]		#3-List in format [month, year, monthTot]
		self.lineage		=	["Unknown","Unknown"]										#2-List, tracks [mother, father] of elephant as elephant-objects
		#self.ancestry		=	[]															#Might add later, stores as a list the % of ancestry elephant has to each biome pop
		
		#Dynamic Factors & Tracking Information
		##Stages:
		##0 - baby, 1 - child, 2 - teenager, 3 - adult  (**ONLY STAGE ABLE TO MAKE BABIES**), 4 - Elder, 5 - Hospiced
		self.age			=	[0,0]						#2-List in format [year-age, month-age]				
		self.lifeStage		=	0							#Tracks developmental stage of elephant
		self.health			=	2							#2-List, ["base health", current health] tracks well being of elephant on a 1 to 10 scale, 0 results in death, < 2 results in higher chances for negative health events
		self.size			=	random.randint(1,5)			#size modifier of elephant, bigger is healthier during good times, but also more likely to die during starvation events, on a 1 to 4 scale	
		self.traits			=	[]							#for (potential) future use, will store elephant's personality traits as list of reference values
		self.conditions		=	[]							#list of 2-lists, special conditions of the elephant (e.g. sickness, close to death, etc.)		
		self.associations	=	[]							#what groups/pods the elephant belongs in
		
		
		#Reproductive Factors & Tracking
		self.fertility		=	[False, 3]					#elephant fertility state, elephant fertility state
		if self.sex == "f":
			self.calfLine	=	[self, "sire"]				#2-list [dam, sire] - tracks length of pregnancy, birth at 22 months +/- 2 months, also tracks lineage
			
		#Life Cycle Notes:
		##ALL PROBABILITIES ARE ANNUAL, monthly probabiilty = prob/12
		#Elephant life cycle stages: Baby [0] => Child [1] => Teen [2] => Adult [3] (**ONLY STAGE ABLE TO MAKE BABIES**) => Elder [4] => Hospice [5]
		#At least one year required between stage transitions
		#Gestation Period:
		#22 months (+/- 2 months)
		#Critical Ages:
		#Baby => Child: 3 - 5
		#Child => Teen: 5 - 10
		#Teen => Adult: 18 - 23
		##Elephants stop bearing calves at 50
		#Adult => Elder: 48 - 53
		#Hospiced: >= 65
		#Death guaranteed by: 100
		#After 65 elephant deaths become much more likely
		
		#Initialization for elephants created as adults (init pop & outsiders)
		if initPop == True:
			diceRoll = random.random()
			if 0 <= diceRoll <= 0.1:
				self.age[0] = random.randint(5, 10)
				self.health += 2
				self.lifeStage = 1
				#print("child made!")
			elif 0.1 < diceRoll <= 0.3:
				self.age[0] = random.randint(11, 18)
				self.health += 3
				self.lifeStage = 2
				#print("teen made!")
			elif 0.3 < diceRoll <= 0.9:
				self.age[0] = random.randint(19, 48)
				self.health += 4
				self.lifeStage = 3
				#print("adult made!")
				if self.sex == "f":
					if random.random() <= 0.8:
						self.fertility[0] = True
					else:
						self.impregnate("Unknown")
						#print("pregnant elephant!")
						for condition in self.conditions:
							if "pregnant" in condition:
								condition[1] = random.randint(1, 21)
			elif 0.9 < diceRoll <= 1.0:
				self.age[0] = random.randint(48, 55)
				self.health += 2
				self.lifeStage = 4
				self.fertility[0] = False
				
			self.birthDay = [random.randint(1, 12), math.floor(monthTot/12) - self.age[0], 0]
			self.birthDay[2] = monthTot - (self.age[0] * 12 + self.birthDay[0])
			self.age[1] = self.age[0]*12 + self.birthDay[0]
		
	#Updates on Annual Birthday
	def upCycle(self):
		upCycle = False
		oldLifeStage = self.lifeStage
		#baby => child transition
		if (self.lifeStage == 0) and (3 < self.age[0] < 5):
			if random.random() <= (1/(3*12)):
				self.lifeStage += 1
				self.health += 1
		elif (self.lifeStage == 0) and (self.age[0] >= 5):
			self.lifeStage == 1
			self.health += 1
			
		#child => teen transition
		elif (self.lifeStage == 1) and (6 < self.age[0] < 10):
			if random.random() <= (1/(4*12)):
				self.lifeStage += 1
				self.health += 2
		elif (self.lifeStage == 1) and (self.age[0] >= 10):
			self.lifeStage == 2
			self.health += 2
		
		#teen => adult transition
		elif (self.lifeStage == 2) and (18 < self.age[0] < 23):
			if random.random() <= (1/(5*12)):
				self.lifeStage += 1
				self.health += 1
				self.fertility[0] = True
		elif (self.lifeStage == 2) and (self.age[0] >= 23):
			self.lifeStage == 3
			self.health += 1
			self.fertility[0] = True
		
		#adult => elder transition
		elif (self.lifeStage == 3) and (48 < self.age[0] < 53):
			if random.random() <= (1/(5*12)):
				self.lifeStage += 1
				self.health -= 2
				self.fertility[0] = False
		elif (self.lifeStage == 3) and (self.age[0] >= 53):
			self.lifeStage == 4
			self.health -= 2
			self.fertility[0] = False
			
		#elder => hospiced transition
		elif (self.lifeStage == 4) and (65 < self.age[0] < 68):
			if random.random() < (1/(3*12)):
				self.lifeStage += 1
				self.health -= 2
		elif (self.lifeStage == 4) and (self.age[0] >= 68):
			self.lifeStage == 5
			self.health -= 2
			
		if self.lifeStage - oldLifeStage != 0:
			upCycle = True
		
		return upCycle
		
	def mate(self, otherElephant):
		diceRoll = random.random()
		#Fail to find partner - waste a fertility level
		if diceRoll <= (1/3):
			self.fertility[1] -= 1
			#print("Didn't get lucky")
		#Find a partner and attempt to mate
		else:
			#If initiator is female
			#print("Oontz!")
			if self.sex == "f":
				otherElephant.fertility[1] -= 1
				self.fertility[1] -= 1
				if random.random() < (1/(5*12)):
					self.impregnate(otherElephant)
			#If initiator is male
			else:
				self.fertility[1] -= 1
				otherElephant.fertility[1] -= 1
				if random.random() < (0.2/12):
					otherElephant.impregnate(self)
				
	def impregnate(self, sire):
		self.conditions.append(["pregnant", 22])
		self.health -= 1
		self.calfLine = [self, sire]
		self.fertility = [False, 0]
		impregnated = True
		#print("Elephant knocked up")
		return impregnated
				
	def pregUpdate(self):
		if self.pregnancy[0] < 22:
			self.pregnancy[0] += 1
		else:
			self.pregnancy[0] = 0
			babyElephant = Elephant(month, monthTot)
			babyElephant.lineage = [self.pregnancy[1], self.pregnancy[2]]
			birth()
					
	def birth(self):
		for condition in self.conditions:
			if "pregnant" in condition:
				self.conditions.remove(condition)
				self.conditions.append(["postpartum", 6])
				self.calfLine = [self, 0]
				self.fertility = [True, -6]
				babyElephant(elephantNum, biomeId, month, monthTot, initPop = False)				
				print("baby born")
				return babyElephant
	
	def sickness(self):
		sickCheck = False
		diceRoll = random.random()
		for condition in self.conditions:
			if "sickness" in condition:
				sickCheck = True
		if sickCheck == False:
			#Normal illness
			if (2 < self.health < 4) and (diceRoll <= 0.05):
				if random.random() <= 0.90:
					self.health -= 1
					self.conditions.append(["mild sickness", random.randint(1, 6)])
					print("elephant got sick")
				else:
					self.health -= 2
					self.conditions.append(["serious sickness", random.randint(1, 3)])
					print("elephant got very sick")					
			#Serious illness more likely if health <= 2
			elif ((self.health <= 2) and (diceRoll < 0.1 * (2 + self.health))) or ((self.health <= 4) and (self.lifeStage == 5) and (diceRoll > 0.1 * (1 + self.health))):
				self.health -= 2
				self.conditions.append(["serious sickness", random.randint(1, 4)])
				print("elephant got very sick")
		
	def recuperate(self):
		for condition in self.conditions:
			if ("postpartum" in condition) and (condition[1] > 0):
				condition[1] -= 1
			elif ("postpartum" in condition) and (condition[1] == 0):
				conditions.remove(condition)
				self.health += 1
				
			if ("sickness" in condition) and (condition[1] > 0):
				self.condition[1] -= 1
			elif ("sickness" in condition) and (condition[1] == 0):
				if condition[1] == "mild sickness":
					self.health += 1
				else:
					self.health += 2
				conditions.remove(condition)
	
	def die(self):
		for association in self.associations:
			association.remove(self)
		#print("elephant died!")
		#print("elephant age:", self.age) 
			
	def updateElephant(self):
		self.age[1] += 1
		if self.age[1]%12 == 0:
			self.age[0] += 1
		if (self.fertility[0] == True) and (self.fertility[1] < 3):
			if (0 < self.fertility[1] < 3) or (self.fertility[1] > 3):
				self.fertility[1] = 3
			else:
				self.fertility[1] += 3
		#if (self.fertility[0] == True) and (self.fertility[1] == 0):
		upCycle = self.upCycle()
		#self.sickness()
		self.recuperate()
		#if self.health <= 0:
		if (self.age[0] >= 65) and (random.random() < (0.2/12)):
			self.die()
			
		return upCycle#, birth)