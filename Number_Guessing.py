from random import randint
from replit import clear
logo = '''        
  _____                   ________         _  __           __             _   
 / ___/_ _____ ___ ___   /_  __/ /  ___   / |/ /_ ____ _  / /  ___ ____  (_)  
/ (_ / // / -_|_-<(_-<    / / / _ \/ -_) /    / // /  ' \/ _ \/ -_) __/ _     
\___/\_,_/\__/___/___/   /_/ /_//_/\__/ /_/|_/\_,_/_/_/_/_.__/\__/_/   (_)    
                                                                              
'''


def play_game():
  ANSWER = randint(0,100)
  clear()
  print(ANSWER)
  print("I HAVE A NUMBER IN MY MIND (0,100)")
  print(logo)
  difficulty = input("choose a difficulty (easy/hard) : ").lower()
  if difficulty == "easy":
    attempts = 10
  else:
    attempts = 5
  while attempts > 0:
    print(f'you have {attempts} attempts left')
    attempts -= 1
    try:
      guess = int(input("guess the number : "))
    except:
      print("YOU ENTERED INVALID INPUT")
      break
    if guess> ANSWER:
      print('TOO HIGH')
    elif guess < ANSWER:
      print('TOO LOW')
    else:
      print(f'YOU GUESSED THE NUMBER IT IS {ANSWER}')
      break
  else:
    print(f'You LOST THE GAME, THE ANSWER WAS {ANSWER}')
  if input("play again (y/n)") == 'y':
    play_game()



    
play_game()