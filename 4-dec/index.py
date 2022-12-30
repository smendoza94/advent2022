# open file in read mode 
file = open("assignmentData.txt","r")

# read file data into a variable
raw_data = file.read()

# split the data by new line in an array
data = raw_data.split("\n")
print(data)