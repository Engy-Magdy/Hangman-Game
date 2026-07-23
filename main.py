import random
words=["good","bad","ugly"]
random_word=random.choice(words)
display_list=["-"]*len(random_word)
display=(" ".join(display_list))
print(display)
print(""" 
      _______
     |/      
     |      
     |      
     |     
     |
    _|___

""")
#Your tries
lives=7
your_guess_letter=[]

#loop for your tries to guess a letterF
while"-"in display and lives>0:
    your_guess=input("Please, guess a letter: ").lower()
#The conditions
    if your_guess in your_guess_letter:
        print("You already guessed that.Try again.")

    else:
        your_guess_letter.append(your_guess)
        if your_guess in random_word:
            for position in range(len(random_word)):
                if random_word[position]==your_guess:
                    display_list[position]=your_guess
                    display=(" ".join(display_list))
        else:
            lives-=1
            if lives==6:
                print("""

      _______
     |/      |
     |      
     |      
     |   
     |
    _|___
""")
            elif lives==5:
             print("""


      _______
     |/      |
     |      (_)
     |    
     |       
     |      
     |
    _|___
""")
             
            elif lives==4:
             print("""


      _______
     |/      |
     |      (_)
     |       |
     |       
     |      
     |
    _|___
""")
            elif lives==3:
             print("""


      _______
     |/      |
     |      (_)
     |      \|
     |       
     |      
     |
    _|___
""")
            elif lives==2:
             print("""


      _______
     |/      |
     |      (_)
     |      \|/
     |       
     |     
     |
    _|___
""")
            elif lives==1:
             print("""


      _______
     |/      |
     |      (_)
     |      \|/
     |      / 
     |       
     |
    _|___
""")
            else:
             print("""
                   
                   You lose!
                   
                   """)
             print("""
      _______
     |/      |
     |      (_)
     |      \|/
     |       |
     |      / \\
     |
    _|___
""")
             break
    print(display)
    print(f"You have {lives} more tries")
if "-"not in display:
    
 print("""
********
YOU WIN!
********
""")
