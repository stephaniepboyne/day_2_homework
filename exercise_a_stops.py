from audioop import reverse


stops = [ "Croy", "Cumbernauld", "Falkirk High", "Linlithgow", "Livingston", "Haymarket" ]

#1. Add "Edinburgh Waverley" to the end of the list
#2. Add "Glasgow Queen St" to the start of the list
#3. Add "Polmont" at the appropriate point (between "Falkirk High" and "Linlithgow")
#4. Print out the index position of "Linlithgow"
#5. Remove "Livingston" from the list using its name
#6. Delete "Cumbernauld" from the list by index
#7. Print the number of stops there are in the list
#8. Sort the list alphabetically
#9. Reverse the positions of the stops in the list
#10 Print out all the stops using a for loop

#1. 
# stops.append("Edinburgh") 

#2. 
# stops.insert(0, "Glasgow Queen St") 

#3. 
# stops.insert(3, "Polmont")

#4. 
# linlithgow_index = stops.index("Linlithgow")
# print(linlithgow_index)

#5. 
# stops.pop(stops.index("Livingston"))
# --OR--
# stops.remove("Livingston")

#6. 
# stops.pop(1)

#7. 
# number_of_stops = len(stops)
# print(number_of_stops)

#8. 
# alphabetical_stops = sorted(stops)
# print(alphabetical_stops)

#9. 
# stops.reverse()
# print(stops)

#10. 
for stop in stops:
    print(stop)







