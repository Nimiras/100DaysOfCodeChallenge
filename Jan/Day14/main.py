# Import all nessecary modules
import random
import art
import game_data

#defineing nessecary variables (points)
print(art.logo)
points = 0
object1 = {}
object2 = {}
playing = True



# function to return a random object from the list of guessable objects
def choose_object():
    unique = False
    #Checks if the object is not one of the already taken object
    while not unique:
        object = game_data.data[random.randint(0,len(game_data.data)-1)]
        if object != object1 and object != object2:
            return game_data.data[random.randint(0,len(game_data.data)-1)]


# function that prints out all the information about the object
def print_information(object, with_follower):
    name        = object["name"]
    description = object["description"]
    country     = object["country"]
    print(f"{name}, {description}, from {country}")
    if with_follower:
        followers = object["follower_count"]
        print(f"Followers (in Million): {followers}")


# function to compare the followers of two objects
def compare(object1, object2, players_choise):
    if players_choise == "h":
        if object2["follower_count"] < object1["follower_count"]:
            return False
        else:
            return True
    elif players_choise == "l":
        if object2["follower_count"] > object1["follower_count"]:
            return False
        else:
            return True



# a while-loop that runs as long the player guesses correctly
# players_choise can only be "h" (Higher) or "l" (lower)
object1 = choose_object()
object2 = choose_object()

    #starting and printing a comparison:
while playing:
    print_information(object1, True)
    print(art.vs)
    print_information(object2, False)

    name_o1=object1["name"]
    name_o2=object2["name"]
    follower_o2 =object2["follower_count"]


    players_choise = input(f"Has {name_o2} more or less follower than {name_o1}? Type 'h' for more and 'l' for less: ")
    if compare(object1, object2, players_choise):
        points += 1
        print(f"{name_o2} has {follower_o2} million followers")
        print("That was correct!")
        temp = object2
        object2 = choose_object()
        object1 = temp
    else:
        print(f"{name_o2} has {follower_o2} million followers")
        print("That was wrong!")
        print(f"You got {points}")
        playing = False
