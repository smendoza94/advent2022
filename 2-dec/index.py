# open file in read mode 
strat_file = open("stratData.txt","r")

# read file data into a variable
strat_data = strat_file.read()

# replace all the /n base text to a ' ' space
# then convert string to list through splitting 
# to be able to manipulate the array  
strat_list = strat_data.replace('\n', ' ').split(" ")

my_score = 0
for i in strat_list:
  if i == 'X':
    my_score += 1
  if i == 'Y':
    my_score += 2
  if i == 'Z':
    my_score += 3

print(my_score)
# close file
strat_file.close()