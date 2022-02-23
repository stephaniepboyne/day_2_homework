users = {
  "Jonathan": {
    "twitter": "jonnyt",
    "lottery_numbers": [6, 12, 49, 33, 45, 20],
    "home_town": "Stirling",
    "pets": [
    {
      "name": "fluffy",
      "species": "cat"
    },
    {
      "name": "fido",
      "species": "dog"
    },
    {
      "name": "spike",
      "species": "dog"
    }
  ]
  },
  "Erik": {
    "twitter": "eriksf",
    "lottery_numbers": [18, 34, 8, 11, 24],
    "home_town": "Linlithgow",
    "pets": [
    {
      "name": "nemo",
      "species": "fish"
    },
    {
      "name": "kevin",
      "species": "fish"
    },
    {
      "name": "spike",
      "species": "dog"
    },
    {
      "name": "rupert",
      "species": "parrot"
    }
  ]
  },
  "Avril": {
    "twitter": "bridgpally",
    "lottery_numbers": [12, 14, 33, 38, 9, 25],
    "home_town": "Dunbar",
    "pets": [
      {
        "name": "monty",
        "species": "snake"
      }
    ]
  }
}

# 1. Get Jonathan's Twitter handle (i.e. the string `"jonnyt"`)
# 2. Get Erik's hometown
# 3. Get the array of Erik's lottery numbers
# 4. Get the species of Avril's pet Monty
# 5. Get the smallest of Erik's lottery numbers
# 6. Return an array of Avril's lottery numbers that are even
# 7. Erik is one lottery number short! Add the number `7` to be included in his lottery numbers
# 8. Change Erik's hometown to Edinburgh
# 9. Add a pet dog to Erik called "Fluffy"
# 10. Add another person to the users dictionary

#1. print(users["Jonathan"]["twitter"])

#2. print(users["Erik"]["home_town"])

#3. print(users["Erik"]["lottery_numbers"])

#4. print(users['Avril']['pets'][0].get("species"))

#5. print(users["Erik"]["lottery_numbers"][2])

#6. 
# even_numbers=[]
# for evens in users["Avril"]["lottery_numbers"]:
#   if evens % 2 == 0:
#     even_numbers.append(evens)
# print(even_numbers)

#7. 
# users["Erik"]["lottery_numbers"].append("7")
# print(users["Erik"]["lottery_numbers"])

#8. 
# users["Erik"]["hometown"] = "Edinburgh"
# print(users["Erik"]["hometown"])

#9. 
# users["Erik"]["pets"].append({
#   "name": "fluffy",
#   "species": "dog"})
# print(users["Erik"]["pets"])

#10.
users["Frodo"] = {
  "twitter" : "frodo10",
  "lottery_numbers": [1, 2, 3, 4, 5, 6, 7],
  "home_town": "Aberdeen",
  "pets": "none"
}

print(users)





