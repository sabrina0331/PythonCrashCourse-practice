import json

filename = 'numbers.json'
with open(filename) as fobs:
    numbers = json.load(fobs)
print(numbers)