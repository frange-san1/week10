# while loop = execute some code WHILE some condtion remains true



###ITERATION### (loop)

# Iterable (There is more than one of that thing)



#Example 1)

# name = input("Enter your name")
# while name == "":
#     print("You did not enter a name")
#     name = input("Enter your name") #Infinite loops are bad
# else:
#     print(f"hello{name}")

#Example 2)

# age = int(input("Enter yours age: "))

# while age <0:
#     print("Age cant be negative")
#     age = int(input("Enter your name: "))
# print(f"You are {age} years old")

#Example 3)

# food = input("enter a food you like (q to quit): ")
# while not food == "q":
#     print(f"you like {food}")
#     food = input ("Enter another food you like (q to quit)")
# print("bye")

#Example 4)

# num = int(input("Enter a # between 1 and 10: "))

# while num < 1 or num >10 :
#     print(f"{num} is not valid")
#     num = int(input("Enter a # between 1 and 10 :"))
# print(f"Your number is {num}")

##########For Loops###########

# for loops = execute a block of code a fixed  number of times
# You can iterate over a range, string, sequence, etc.

# for x in reversed(range(1, 11, 2)):    # Prints 10-1, skipping every 2nd #
#     print(x)
# print("HAPPY NEW YEAR!")

# credit_card = "1234-5678-9012-3456"
# for x in credit_card:
#     print(x)

# for x in range(1,21):
#     if x == 13 or x == 15 or x == 20:
#         break
#     else:
#         print(x)


# Create a list of famous horror movie characters
# horror_characters= ["Freddy Kruger", "Jason Voorhees", "Micheal Myers", "Pennywise", "Chucky"]
#iterate throught the list and print each character

# for character in horror_characters:
#     if character == "Jason Voorhees":
#         continue
#     print(character)

# for character in horror_characters:
#     if character == "Micheal Myers":
#         character = "Dracula"
#     if character == "Pennywise":
#         character = "Ghost Face"
# print(character)


#Create a list of famous horror movies
#Iterate throught the list and if a certain movie is found, break list
#Print out the rest of the movies
#next replace one of the movies with a movie you like 

horror_movies = ["Chucky", "Halloween", "Scream", "IT"]
for movie in horror_movies:
    if movie == "Scream":
        movie = ""
    else:
        print(movie)
    if movie == "IT":
        movie = "Friday the 13th"
        print(movie)