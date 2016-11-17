import random
words = [
    'stuff',
    'magic',
    'dreams',
    'vision',
    'doves',
    'determination'
]

while True:
    # make a list of words
    start = input("Press enter/return to start, or enter Q to quit: ")
    if start.lower() == 'q':
        break
    
    # pick a random word
    secret_word = random.choice(words)
    bad_guess = []
    good_guess = []
    
    while len(bad_guess) < 7 and len(good_guess) != len(list(secret_word)):
        # draw guess letters, spaces and strikes
        for letter in secret_word:
            if letter in good_guess:
                print(letter, end='')
            else:
                print('_',end='')
        print('')
        print('Strikes: {}/7'.format(len(bad_guess)))
        print('')
        
        # take guess
        guess = input("Guess a letter: ").lower()
        
        if len(guess) != 1:
            print("You can only guess a single letter!")
            continue
        elif guess in bad_guess or guess in good_guess:
            print("You've already guessed that letter!")
            continue
        elif not guess.isalpha():
            print("You can only guess letters!")
            continue

        # print out win/lose
        if guess in secret_word:
            good_guess.append(guess)
            if len(good_guess) == len(list(secret_word)):
                print("You win! The word was {}".format(secret_word))
                break
        else:
            bad_guess.append(guess)
    else:
        print("You didn't guess it! My secret word was {}".format(secret_word))
