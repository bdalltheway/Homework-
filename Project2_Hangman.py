#  _______ 
#  |      |
#  0      |
# /|\     |
#  |      | 
# / \     |
def gameBoard(score):
    for i in range(7):
        if i == 0: 
            print(" ________")
        if i == 1:
            print(" |      |")
        if i == 2:
            if score > 0:
                print(" 0      |")
            else: 
                print("        |")
        if i == 3:
            if score > 3:
                print("/|\     |")
            elif score > 2: 
                print("/|      |")
            elif score > 1: 
                print("/       |")
            else: 
                print("        |")
        if i == 4:
            if score > 4:
                print(" |      |") 
            else:
                print("        |")
        if i == 5:
            if score > 5:
                print("/ \     |")
            elif score > 4: 
                print("/       |") 
            else:
                print("        |") 

mainWord = (input("Player 2: What word would you like to choose? ")).upper()
print()
print()
print()
print()
print()
print()
print()
print()
print()
print()
print()
print()
print()
print()
print()
print()
print()
print()

guessWord = []
for letters in range(len(mainWord)):
    guessWord.append("_")
score = 0 


while score < 6:
    
    gameBoard(score)
    for x in guessWord:
        print(x + " ", end="")
    print()
    
    choice = (input("Player 1: What letter would you like to guess? ")).upper()
    if choice in mainWord:
        print("Correct!")
    else: 
        print("Sorry, wrong answer!")
        score += 1
    
    for d in range(len(mainWord)):
        if choice == mainWord[d]:
            guessWord[d] = choice 
           
   
            

print("The End!")

