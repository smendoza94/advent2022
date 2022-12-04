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

# PART 1
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
print('my intial score: ' + str(my_score)) # prints 14827

#PART 2
# new conditions were given where X means lose, Y draw, and Z win
# lose -> [A = Z +3], [B = X +1], [C = Y +2]
# draw -> [A = X +1], [B = Y +2], [C = Z +3]
# win -> [A = Y +2], [B = Z +3], [C = X +1]
new_score = 0
for i in matches:
  # X means lose +0
  if i[1] == 'X':
    new_score += 0
    # lose to rock play scissors +3
    if i[0] == 'A':
      new_score += 3
    # lose to paper play rock +1
    elif i[0] == 'B':
      new_score += 1
    # lose to scissors play paper +2
    elif i[0] == 'C':
      new_score += 2
  # Y means draw +3
  elif i[1] == 'Y':
    new_score += 3
    # draw to rock +1
    if i[0] == 'A':
      new_score += 1
    # draw to paper +2
    elif i[0] == 'B':
      new_score += 2
    # draw to scissors +3
    elif i[0] == 'C':
      new_score += 3
  # Z means win +6 
  elif i[1] == 'Z':
    new_score += 6
    # win to rock play paper +2 
    if i[0] == 'A':
      new_score += 2
    # win to paper play scissors +3
    elif i[0] == 'B':
      new_score += 3
    # win to scissors play rock +1
    elif i[0] == 'C':
      new_score += 1

print('my new score is: ' + str(new_score)) # points 13889

# close file
file.close()