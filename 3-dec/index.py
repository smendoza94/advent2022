# open file in read mode 
file = open("contentsData.txt","r")

# read file data into a variable
data = file.read()

# split the data by new line in an array
list = data.split("\n")

# divide each rutsack into the two equal compartments 
# ie. [['Aasawdea','awaWdasd'],['adwD','adkW'],...]
rutsacks = []
for i in list:
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
