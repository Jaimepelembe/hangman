from random import choice, randint
from hangmanArt import hangmanStages, message
from hangmanWords import dictWords


#Todo 1: Randomly choose a topic and then a word from the dictWords

dictKey=choice(list(dictWords.keys()))
indexList=randint(0,len(dictWords[dictKey])-1)
wordSelected= dictWords[dictKey][indexList]
life=6
isGuessed= False


#Functions
def reduceLife(life):
    """Reduces the player lives in one unit and return the life."""

    life-=1

    if life < 1:
        print(f"=================Voce Perdeu================= \nA palavra era {wordSelected}")

    else:
        print(f"Você digitou {letterGuessed}, que nao esta na palavra. Voce perdeu uma vida.")

    return life

def drawHangman(life):
    """Print the current stage of the hangman"""
    if life >=0:
        print(hangmanStages[life])


print(message)
print(f"O tópico da palavra é {dictKey}")

wordToGuess=""
for i in range(0, len(wordSelected)):
    wordToGuess+="_"
correctLetters=list(wordToGuess)

while not isGuessed and life>0:
    #print(wordSelected)
    print(f"*****************{life}/6 Vidas*****************")
    print(f"Palavra a adivinhar: {wordToGuess}")
    letterGuessed=input("Adivinhe uma letra: ").lower()

   
    if letterGuessed in wordSelected:
        if letterGuessed in correctLetters:
            print(f"Você já escolheu {letterGuessed}")
        else: # The user typed a new letter that is on the word selected.
            for i,char in enumerate(wordSelected):
                if char == letterGuessed:
                    correctLetters[i]=char 

    else: # The user typed a letter that is not in the word selected.
        life=reduceLife(life)

    drawHangman(life)

     # The word is Guessed?
    wordToGuess="".join(correctLetters)
    if wordSelected == wordToGuess:
        print(f"=================Voce Venceu================= \nA palavra e: {wordToGuess}")
        isGuessed=True
    

