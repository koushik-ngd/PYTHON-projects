print('MY FIRST PYTHON PROJECT')
print("Python quiz game")

play = input("Do you want to play? Y or N \n")

if play != "Y":
    quit()

print("Great! Let us begin...")
total_score = 0

answer1 = input("Which country has the highest life expectancy? \n")

if answer1 == "Hong Kong" or "HONG KONG" or "hong kong" or "hongkong":
    print("Good job!")
    total_score = total_score + 1
else:
    print("Incorrect!")


answer2 = input("Who was the Ancient Greek God of the Sun?")

if answer2 == "Apollo" or "APOLLO" or "apollo":
    print("Good job!")
    total_score = total_score + 1
else:
    print("Incorrect!")


answer3 = input("How many minutes are in a full week?")

if answer3 == "10,080" or "10080":
    print("Good job!")
    total_score = total_score + 1
else:
    print("Incorrect!")


answer4 = input("How many faces does a Dodecahedron have?")

if answer4 == "Twelve" or "12":
    print("Good job!")
    total_score = total_score + 1
else:
    print("Incorrect!")

    
answer5 = input("What art form is described as a decorative handwriting or a handwritten lettering? ")

if answer5 == "Calligraphy" or "CALLIGRAPHY" or "calligraphy":
    print("Good job!")
    total_score = total_score + 1
else:
    print("Incorrect!")


answer6 = input(" What is acrophobia a fear of? ")

if answer6 == "Heights" or "HEIGHTS" or "heights":
    print("Good job")
    total_score = total_score + 1
else:
    print("Incorrect!")

    
answer7 = input("What is a word, phrase, number, or other sequence of characters that reads the same backward as forward?")

if answer7 == "Palindrome" or "PALINDROME" or "palindrome":
    print("Good job")
    total_score = total_score + 1
else:
    print("Incorrect!")

    
answer8 = input("What is the name of the Chinese philosophical system that emphasizes harmony with nature?")

if answer8 == "Taoism" or "TAOISM" or "taoism":
    print("Good job!")
    total_score = total_score + 1
else:
    print("Incorrect!")

    
answer9 = input("What is the smallest U.S. state by area?")

if answer9 == "Rhode Island" or "RHODE ISLAND" or "rhode island":
    print("Good job!")
    total_score = total_score + 1
else:
    print("Incorrect!")


answer10 = input("What is the outermost layer of the Earth’s atmosphere called?")

if answer10 == "Exosphere" or "EXOSPHERE" or "exosphere":
    print("Good job!")
    total_score = total_score + 1
else:
    print("Incorrect!")

print("Your total score is: ", total_score)

if(total_score < 5):
    print("Better luck next time! Keep it up!")
if(total_score > 5 and total_score < 10):
    print("You have done well!")
if(total_score == 10):
    print("Outstanding!")

print("The end. Thanks for joining")


    