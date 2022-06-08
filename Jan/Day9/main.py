#from replit import clear
import art
#HINT: You can call clear() to clear the output in the console.

def maxdic(dic):
    max = 0
    name = ""
    for item in dic:
        if dic[item] > max:
            max = dic[item]
            name = item
    return name


print(art.logo)
print("Welcome to the secret auction program.")
betting = True
bettings = {}
while betting:
    name = input("What is your name?: ")
    bit = input("What is your bid?: ")
    bettings[name] = int(bit)
    answer = input("Are there any other bidders? Type 'yes' or 'no'")
    if answer == "no":
        betting = False
    #clear()
print(f"The winner is {maxdic(bettings)} with a bit of {bettings[maxdic(bettings)]}$")
