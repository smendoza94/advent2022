# open file in read mode 
calories_file = open("caloriesData.txt","r")

# read file data into a variable
calories_data = calories_file.read()

# convert string to list through splitting
calories_list = calories_data.replace('\n', ' ').split(" ")

# 
lists =[[]]
for i in calories_list:
  if i == ' ':
    lists.append([])
  else:
    lists[-1].append(i)

# close file
calories_file.close()