import random

#Importiert die Hangman Zeichen und eine Liste von möglichen Worten
import hangman_art
import hangman_words


#Ueberprueft, ob alle Buchstaben erfolgreich geraten wurden.
def checkStatus(display):
    for i in display:
        if (display.count("_") > 0):
            return False
    return True

# Ein Wort wird aus einer Liste gewählt
choosen_word = hangman_words.word_list[random.randint(0, len(hangman_words.word_list))]
print(choosen_word)
# Die leeren Zeichen werden generiert
display = []
for i in range(len(choosen_word)):
    display += "_"

##########################
# Hier beginnt das Spiel #
##########################

#Der Spieler hat sechs Leben
lives = 6
#Es wird eine Liste erstellt, in der die bereits geratenen Buchstaben gespeichert werden
already_guessed_letters = []
# Ausgabe des Titelbildschirms:
print(hangman_art.logo)

#Das Spiel geht solange der Spieler noch Leben hat und leehre Stellen im zu ratenem Wort sind
while (lives > 0 and not checkStatus(display)):

    # Eingabe durch den User
    letter = input("Guess a letter: ")

# Prüft, ob der Benutzer den richtigen Buchstaben erraten hat, und wenn ja, wird dieser
# durch den eingegebenen Buchstaben ersetzt
    for i in range(len(choosen_word)):
        if letter.lower() == choosen_word[i]:
            display[i] = letter

    # Wenn der Spieler einen falschen Buchstaben geraten hat, so wird ihm ein Leben abgezogen
    if letter not in choosen_word:
        lives -= 1
    else:
        #Danach wird geschaut, ob der Spieler den Buchstaben schon geraten hat,
        #indem in die Liste der bereits geratenen Buchstaben genschaut wird, ob sich der Buchstabe
        #schon in der Liste befindet
        if letter in already_guessed_letters:
            #Wenn ja, wird eine Nachricht ausgegeben, die dies dem Spieler zu verstehen gibt
            print ("You already guessed that letter!")
        else:
            #Falls nicht, so wird der vorhin geratene Buchstabe zu der Liste der bereit geratenen hinzugefuegt
            already_guessed_letters += letter

    #Ausgabe der Galgenmaennchens und der Buchstaben mit den Luecken
    print(display)
    print(hangman_art.stages[lives])

# Ausgabe nach dem Sieg oder der Niederlage
if lives == 0:
    print("You lose!")
else:
    print("You won!")
