class Elephant:

	def __init__(self, month):
		#Elephant Tracking Information
		self.trackid		=	0							#equivalent of name,
		self.elephantNum	=	0							#lists elephant #, simpler than trackid
		self.sex			=	random.choice("m", "f")		#0 for female, 1 for male
		self.age			=	[0,0]						#2-List in format [year-age, month-age]				
		self.birthday		=	[month,0]					#2-List in format [month, year]
		
		#Stages
		#0 - baby
		#1 - child
		#2 - teenager
		#3 - adult
		#4 - Senior
		#5 - Hospice
		self.lifeStage		=	0
		
		self.health			=	4				#tracks well being of elephant on a 1 to 10 scale, 0 results in death, < 2 results in higher chances for negative health events
		self.size			=	0				#size of elephant, bigger is 
		
		self.pregnancy		=	0				#tracks length of pregnancy, birth at 22 months +/- 2 months
		self.fertility		=	0				#fertility rate of elephants
		
		self.traits			=	0				#for (potential) future use, will store elephant's personality traits as list of reference values
		self.conditions		=	0				#special conditions of the elephant (e.g. sickness, close to death, etc.)
		
		#Life Cycle Notes:
		##ALL PROBABILITIES ARE ANNUAL, monthly probabiilty = prob/12
		#Elephant life cycle stages: Baby => Child => Teen => Adult => Senior => Hospice
		#At least one year required between stage transitions
		#Gestation Period:
		#22 months (+/- 2 months)
		#Critical Ages:
		#Baby => Child:
		#3: 25%
		#4: 50%
		#5: 25%
		#Child => Teen:
		#5 - 6: 10% (20%)
		#7 - 8:  25% (50%)
		#9 - 10: 15% (30%) - all elephants become teens by 11
		#Teen => Adult:
		#18 - 19: 10% (20%)
		#20 - 21: 25% (60%)
		#22 - 23: 10% (20%) - all elephants start breeding by 24
		##Elephants stop bearing calves at 50
		#Adult => Elder:
		#48 - 49: 15% (30%)
		#50 - 51: 30% (60%)
		#51 - 53: 5% (10%)
		#Extreme Elder - Death:
		#After 65 elephant deaths become much more likely
		
	
	def upCycle(self):
		self.lifeCycle += 1
		
			
	def update(self):
		self.age[1] += 1
		if self.age[1]%12 == 0:
			self.age[0] += 1
		
		if self.sex == "f":
			
			
		#		
		if self.lifeCycle == 3:
			if self.
		
		#
		if 3 <= self.age[0] < 5:
			if stage[]
			
			self.upCycle()
		
		#
		elif 5 <= self.age[0] < 10:
			self.upCycle()
		
		#
		elif 18 <= self.age[0] < 23:
			self.upCycle()
		
		#
		elif (((self.age[0] == 24) and (self.lifeCycle != 3))):
		
			self.upCycle()
		
		#
		elif 48 <= self.age[0] < 53:
			self.cycle
			self.upCycle()
		
		#
		elif 65 == self.age[0]:
			self.upCycle()
		
		
	def mating(elephant):
		
	
	def pregnancyTrack():
		self.
	
