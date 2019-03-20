import ElephantReserve

def main():
	print("test")
	reserve = ElephantReserve.ElephantReserve(name = "Elephant Reserve", mapSize = 1)
	for year in range(20):
		reserve.updateReserve()
		print(reserve.map)
		input()
		
if __name__ == "__main__":
	main()