# open file in read mode 
strat_file = open("stratData.txt","r")

# read file data into a variable
strat_data = strat_file.read()

# replace all the /n base text to a ' ' space
# then convert string to list through splitting 
# to be able to manipulate the array  
strat_list = strat_data.replace('\n', ' ').split(" ")
print(strat_list)

# close file
strat_file.close()