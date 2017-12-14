import random
from sys import exit


print("This script generates random GPS points in a square area and saves the output as a CSV.\nPlease enter Lat and Long values for opposite corners of the square area:")



lat1 = input("Enter Lat value for corner #1 with significant figures (e.g. 40.7000) >>> ")
lon1 = input("Enter Long value for corner #1 with significant figures (e.g. -74.2000) >>> ")
lat2 = input("Enter Lat value for corner #2 with significant figures (e.g. 40.8000) >>> ")
lon2 = input("Enter Long value for corner #2 with significant figures (e.g. -73.9200) >>> ")
randVar = input("Would you like an additional random variable for each entry? (\"Y\"/\"N\") >>> ")

if randVar == "Y" or randVar == "y":
	randVar = True
	randValueLow = input("Enter lowest acceptable value for random variable (e.g. \"-10\") >>> ")
	randValueHigh = input("Enter Highest acceptable value for random variable (e.g. \"1000.0001\") >>> ")
elif randVar == "N" or randVar == "n":
	randVar = False

else:
	print("Error: Please use Y or N to indicate response")
	exit(0)


num_points = input("Enter number of points to be generated (e.g. 1000) >>> ")

try:
	lat1 = float(lat1)
	lon1 = float(lon1)
	lat2 = float(lat2)
	lon1 = float(lon1)
	num_points = int(num_points)
	if randVar == True:
		randValueLow = float(randValueLow)
		randValueHigh = float(randValueHigh)

except:
	print("Error: Please enter numbers")
	exit(0)



for i in range(num_points):
	line =[]
	thisLat = random.uniform(float(lat1), float(lat2))
	thisLon = random.uniform(float(lon1), float(lon2))
	line.append(str(thisLat))
	line.append(str(thisLon))

	if randVar == True:
		line.append(str(random.uniform(randValueLow, randValueHigh)))
	else:
		pass

	printline = ','.join(line)
	print(printline)

exit(0)