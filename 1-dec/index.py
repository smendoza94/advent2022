# open file in read and read data
caloriesDataFile = open("caloriesData.txt","r")

caloriesData = caloriesDataFile.read()

# print data
print(caloriesData)
caloriesDataFile.close()