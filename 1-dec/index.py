import requests

url = 'https://adventofcode.com/2022/day/1/input'
response = requests.get(url)

with open ('caloriesData.txt','wb') as f:
  f.write(response.content)