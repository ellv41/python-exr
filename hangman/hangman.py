import random
import time
from hangman_words import word_list
logo = '''
**************************** 
****** PLAY HANG--MAN ******     
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========         
****************************    
'''


# func for random choosing a frase from the list word_list
def choose_frase():
    disp_word = []
    chos_word = random.choice(word_list)
    for lt1 in chos_word:
        if lt1 == " ":
            disp_word += ","
        else:
            disp_word += "_"
    return chos_word, disp_word


# func game play : score  -1 point for wrong guss , +5 for correct guss
def game_play(chosen_frase, display_frase, g_score):
    # number of errors (limit to 20 errors)
    err = 1
    while display_frase.count("_") and err <= 20:
        # guessed letter could be upper or lower
        guessed_ltr = input("guss a letter : ").lower()
        if guessed_ltr in display_frase:
            print(f"You've already guessed {guessed_ltr}")
        wrong_answer = True
        for x in range(0, len(chosen_frase)):
            if chosen_frase[x].lower() == guessed_ltr:
                display_frase[x] = guessed_ltr
                wrong_answer = False
                # for each correct letter found 5 points
                g_score += 5
        if wrong_answer:
            print(f'Error number {err}')
            err += 1
            g_score -= 1
        print(f"{' '.join(display_frase)}")
    if display_frase.count("_"):
        return None, g_score
    else:
        return 1, g_score


#    main program  #
play_again = ""
total_score = 0
while not (play_again == "x" and play_again == "X"):
    score = 0
    print(f'{logo}')
    chosen_fr, display_fr = choose_frase()
    start_time = int(time.time())
    print(f'start game time {time.strftime(format("%H:%M:%S"))}')
    print(f"Guss the Frase  :   {' '.join(display_fr)} ")
    win_game, score = game_play(chosen_fr, display_fr, score)
    end_time = int(time.time())
    game_time = int(end_time - start_time)
    if win_game:
        if game_time < 31:
            score += 100
        print(f'***** you guessed it , your score is : {score} \n end Game at = {time.strftime(format("%H:%M:%S"))}'
              f' Game time =  {game_time}')
    else:
        print("End of the Game you lost , the word was : " + chosen_fr + f' your score is : {score} '
                                                                         f'end time = {time.strftime(format("%H:%M:%S"))}'
                                                                         f' game time =  {game_time}')
    total_score += score
    play_again = input("to continue playing press Enter , to quit enter x")
#    end main   #



