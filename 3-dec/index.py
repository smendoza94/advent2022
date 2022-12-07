import string

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
group_rutsacks = []
temp_group = []
for i in data:
  if (data.index(i)+1)%3 == 0:
    group_rutsacks.append(temp_group)
    temp_group = []
  temp_group.append(i)

