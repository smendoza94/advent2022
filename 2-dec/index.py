# open file in read mode 
file = open("stratData.txt","r")

# read file data into a variable
data = file.read()

# split the data by new line and place each letter pair 
# into an array for each match ie. [['A','Y'],['B','X'],...]
list = data.split("\n")
matches = []
for i in list:
  matches.append([i[0],i[2]])

# rules state points are given based on the hand played
# add those points accordingly
hand_points = 0
for i in matches:
  if i[1] == "X":
    hand_points += 1
  elif i[1] == "Y":
    hand_points += 2
  elif i[1] == "Z":
    hand_points += 3
  else:
    print('error, my hand was: ' + str(i[1]))

# rules state points are given during win +6, lose +0, or draw +3
match_points = 0
for i in matches:
  # if win gain six points
  if (i[0] == 'A' and i[1] == 'Y') or (i[0] == 'B' and i[1] == 'Z') or (i[0] == 'C' and i[1] == 'X'):
    match_points += 6
  # if draw win three points
  elif (i[0] == 'A' and i[1] == 'X') or (i[0] == 'B' and i[1] == 'Y') or (i[0] == 'C' and i[1] == 'Z'):
    match_points += 3
  # if lose no points
  elif (i[0] == 'A' and i[1] == 'Z') or (i[0] == 'B' and i[1] == 'X') or (i[0] == 'C' and i[1] == 'Y'):
    match_points += 0
  else:
    print('missed match: ' + str(i[0]) + str(i[1]))

# now sum the total of points from hand and match as my_score and print
my_score = hand_points + match_points
print('my total score: ' + str(my_score)) # prints 14827

# close file
file.close()