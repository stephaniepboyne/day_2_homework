from curses import keyname
from itertools import count
from multiprocessing.sharedctypes import Value


united_kingdom = [
  {
    "name": "Scotland",
    "population": 5295000,
    "capital": "Edinburgh"
  },
  {
    "name": "Wales",
    "population": 3063000,
    "capital": "Swansea"
  },
  {
    "name": "England",
    "population": 53010000,
    "capital": "London"
  }
]

# 1. Change the capital of Wales from `"Swansea"` to `"Cardiff"`.
# 2. Create a dictionary for Northern Ireland and add it to the `united_kingdom` list (The capital is Belfast, and the population is 1,811,000).
# 3. Use a loop to print the names of all the countries in the UK.
# 4. Use a loop to find the total population of the UK.

#1. 
# (united_kingdom[1]["capital"]) = "Cardiff"
# print(united_kingdom[1]["capital"])

#2. 
# united_kingdom.append({ 
#   "name": "Northern Ireland",
#   "population": 1811000,
#   "capital": "Belfast"
# })
# print(united_kingdom)

#3. 
# for names in united_kingdom:
#   print(names["name"])

#4. 
total_pop = 0

for pops in united_kingdom:
  total_pop += pops["population"]
  pops["population"] = 0 

print(total_pop)


    
 





