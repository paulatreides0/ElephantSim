import ElephantReserve
import time

def main(mapSize, simLen):
	print("TESTING")
	print("")
	reserve = ElephantReserve.ElephantReserve(name = "Elephant Reserve", mapSize = mapSize)
	reserve.census(initCheck = True)
	for month in range(simLen*12):
		reserve.updateReserve()
	
		
		
if __name__ == "__main__":
	main(1, 200)