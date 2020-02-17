import random
 
def get_secret_word(word_file="/usr/share/dict/words"):
    good_words = []
    with open(word_file) as f:
        for word in f:
            word = word.strip()
            if not word.isalpha():
                continue
            if len(word) < 5:
                continue
            if word[0].isupper():
                continue
            good_words.append(word)
 
    word = random.choice(good_words)
    return word.lower()

def hide_word(s,l):
	hide_word = []
	for i in s:
		if(i in l):
			hide_word.append(i)
		else:
			hide_word.append('_')
	return ''.join(hide_word)
    
def guesses(l):
    guess = []
    for i in l:
        if( i not in guess):
            guess.append(i)
    return ' '.join(guess)


def chances(s,l,new_item,turns):
    if(new_item not in l):
            if(new_item not in s):
                turns -= 1
    return turns


def status_message(s,l,new_letter, turns):
    if(new_letter not in l):
        l.append(new_letter)
    
    if('_' not in hide_word(s, l)):
        message = """{}

guesses    : {}
chances    : {}
Message    : You Win!!""".format(hide_word(s, l), guesses(l), turns)
        return message, True
    
    if (turns == 0):
        message = """{}

guesses    : {}
chances    : {}
Message    : You Lose!! word : {}""".format(hide_word(s, l), guesses(l), turns, s)
        return (message, True)

    message = """{}

guesses    : {}
chances    : {}""".format(hide_word(s, l), guesses(l), turns)
    return (message, False)

    
def main():
    l = []
    turns = 7
    game_over = False
    new_item = ''
    sw =  get_secret_word()
    print (sw)
    message, game_over = status_message( sw, l, new_item, turns)
    print(message)
    while (game_over == False):
        
        new_item = input("enter letter ")
        turns = chances(sw,l,new_item,turns)
        message, game_over = status_message( sw, l, new_item, turns)
        print(message)
       
if(__name__ == '__main__'):
    main()
