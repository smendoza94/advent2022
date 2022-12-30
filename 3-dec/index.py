import string
from itertools import zip_longest

# open file in read mode 
file = open("contentsData.txt","r")

# read file data into a variable
raw_data = file.read()

# split the data by new line in an array
data = raw_data.split("\n")

# PART 1
# divide each rutsack into the two equal compartments 
# ie. [['Aasawdea','awaWdasd'],['adwD','adkW'],...]
rutsacks = []
for i in data:
  compartment_pair = [i[slice(0,len(i)//2)],i[slice(len(i)//2,len(i))]]
  rutsacks.append(compartment_pair)

# compare each rutsack between its two compartments and find 
# the common item "letter" in each compartment
common_items = []
for i in rutsacks:
  for j in i[0]:
    if j in i[1]:
      common_items.append([j])
      break

# convert letters to points and total for submital 
alphabet = list(string.ascii_letters)
points = []
for i in common_items:
  points.append(int(alphabet.index(i[0]))+1)
total_points = sum(points)
print(total_points) # prints 8139

# PART 2
# divide each groups of 3 rutsucks into their own arrays
# group_rutsacks = []
# for i in data:
#   if (data.index(i))%3 == 0:
#     group_rutsacks.append(temp_group)
#     temp_group = []
#   else:
#     temp_group.append(i)

# this solution was recommended by chatGPT AI and modified by developer
def group_by_three(array):
  return zip_longest(*[iter(array)]*3)
group_rutsacks = [group for group in group_by_three(data) if None not in group]

# compare each groups three rutsacks and find 
# the common item "letter" between their rutsacks
# group_common_items = []
# for i in group_rutsacks:
#   print(i)
#   for j in i[0]:
#     if j in i[1]:
#       if j in i[2]:        
#         group_common_items.append([j])
#         break

# ChatGPT: This code converts each string into a set, 
# and then uses the intersection method to find the common elements.
group_common_items = []
for i in group_rutsacks:
  group_common_items.append(set(i[0]).intersection(set(i[1])).intersection(set(i[2])))
print(group_common_items)