# open file in read mode 
calories_file = open("caloriesData.txt","r")

# read file data into a variable
calories_data = calories_file.read()

# replace all the /n base text to a ' ' space
# then convert string to list through splitting 
# to be able to manipulate the array  
calories_list = calories_data.replace('\n', ' ').split(" ")

# convert the strings in the arry into 

# seperate each elf's listed calories into their own array by using 
# the empty '' so that we can sum up each total
elf_calorie_lists =[[]]
for i in calories_list:
  if i == '':
    elf_calorie_lists.append([])
  else:
    i = int(i)
    elf_calorie_lists[-1].append(i)
print(elf_calorie_lists)

# close file
calories_file.close()