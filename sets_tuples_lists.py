# collection + single "variable" used to store multiple values
#  list = [] ordered and changeable. Duplicates OK. 
#  set= {} unordered and immutable, but Add/Remove OK. NO duplicates
#  Tuble = () ordered and unchangeable. Duplicates OK. Faster 

#########################################################
#SETS
#fruits = {"apple", "orange", "banana", "coconut",}

#print(dir(fruits))
#print(help(fruits))
#print(len(fruits))
#print("pineapple" in fruits)

##########################################################
#TUBLES

#fruits = ("apple", "orange", "banana", "coconut",)

#print(dir(fruits))
#print(help(fruits))
#print(len(fruits))
#print("pineapple" in fruits)

#print/(fruits.index("apple"))
#print(fruits.count("coconut"))

#print(fruits)
#for fruit in fruits:
    #print(fruit)

##########################################################
#DICTIONARY = a collection of {key:value} pairs
             #ordered and changable. No duplicates
capitals = {"USA": "Washington D.C.",
            "India": "New Delhi",
            "China": "Beijing",
            "Russia": "Moscow"}

#print(dir(capitals))
#print(help(capitals))
#print(capitals.get("USA")) #gives the value of the key
#print(capitals.get("Japan")) #is not in our dictionary, gives no key

#if capitals.get("China"):
    #print("That capital exists")
#else:
   #print("That capital dosent exist")

#capitals.update({"Germany": "Berlin"})
#capitals.update({"Mexico": "Mexico City"})
#capitals.pop("China")
#capitals.popitem()
#capitals.clear

#keys= capitals.keys()

#for key in capitals.keys():
    #print(key)

#values = capitals.values()
#for value in capitals.values():
    #print(value)

items = capitals.items()
for key, value in capitals.items():
    print(f"{key}: {value}")











#print(fruits[0]) #gives an error 
#fruits.add("pineapple") #adds to the variable
#fruits.add("strawberry") 
#fruits.remove("apple") #removes from the variable
#fruits.pop() #removes the last one, pops it off
#fruits.clear() #clears the variable



# fruits[0] = "pineapple" # I can reassing values using this
# fruits.append("pineapple")
# fruits.remove("apple")
# fruits.insert(0, "pineapple")
# fruits.sort()
# fruits.reverse()
# fruits .clear()

#print(fruits.index("coconut"))

#print(fruits)

# print(fruits[0])
# for fruit in fruits:
#    print(fruit)

#cars = ["bmw", "maserati", "audi", "mercedes", "ferrari"]
#print(f"these are list of {cars}")
#print(f"the first car is {cars[0]}")


#changing the vaule of the list
#cars[0]= "toyota"
#print(f"the first car is {cars[0]}")


#print(f"the last car is {cars[-1]}")
#cars[-1] = "lamborghini"
#print(f"the last car is {cars[-1]}")

#adding a value to the list
#cars.append("bugatti")
#print(cars)

#cars.remove("maserati")
#print(cars)

# looping through the list 
# otherwise called iterating through the list 
#for car in cars:
   # print(len(car))
    #print(car)
   # carRequest = input("add a new car please: ")
   # cars.append(carRequest)
   # print(cars)
   # print(len(cars))
    # print(cars.upper())
  #  print(cars)
# if len(cars) >10:
#  break



#challenge
# create a list of friends
# make sure the initial list is none 
#friends = []
# add a new friend to the list, add at least 5 friends
# remove a friend
# insert a friend
# insert a friend at a specific index maybe 2
# print the list of friends
# loop through the list and print the friends name
# see if a particular friend is in the list (boolean value)
# if the list is greater than 10 break the loop

#friends = ["Marco", "Jesus", "Delan", "Jared", "Abel"]
#friends.remove("Marco")
#friends.append("Damian")
#friends.insert(1, "David")
#print(friends)
#for friends in friends:
   # print(friends)

#print("Jared" is friends)