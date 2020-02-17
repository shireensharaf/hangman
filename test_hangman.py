import hangman

def test_secret_word_no_punctuation():
    with open("/tmp/words.txt","w") as f:
        for i in ["word'one", "word_two", "wordthree"]:
            f.write(i+"\n")
    selected_word = hangman.get_secret_word('/tmp/words.txt')
    assert selected_word == "wordthree"
 
def test_secret_word_atleast_five():
    with open("/tmp/words.txt","w") as f:
        for i in ["wo", "wor", "word", "bigword"]:
            f.write(i+"\n")
    selected_word = hangman.get_secret_word('/tmp/words.txt')
    assert selected_word == "bigword"
 
def test_secret_word_lowercase():
    with open("/tmp/words.txt","w") as f:
        for i in ["Wording", "wOrding", "WORDING", "wording"]:
            f.write(i+"\n")
    selected_word = hangman.get_secret_word('/tmp/words.txt')
    assert selected_word == "wording"
 
def test_secret_word_no_repeat():
    with open("/tmp/words.txt","w") as f:
        for i in ["disaster","recall","advise","national","infrastructure","shots","fired", "federation", "duress"]:
            f.write(i+"\n")
    l = []
    for i in range(3):
        l.append(hangman.get_secret_word('/tmp/words.txt'))
    assert len(set(l)) == 3


def test_hide_word_no_guesses():
    assert hangman.hide_word("elephant",[]) == "________" 

def test_hide_word_single_correct_guess():
    assert hangman.hide_word("elephant",['l']) == "_l______"

def test_hide_word_2():
    assert hangman.hide_word("elephant", ['l','e','z']) == "ele_____"



def test_full_chance():
	assert hangman.chances('elephant', [],'',7) == 7

def test_1_wrong():
	assert hangman.chances('elephant', [],'x',7) == 6

def test_multiple():
	assert hangman.chances('elephant', ['e','x','l'],'r',6) == 5

def test_multiple_repeat():
	assert hangman.chances('elephant', ['e','x','l','r'],'x',5) == 5


def test_no_input():
    message, game_over = hangman.status_message("elephant", [],'', 7)
    assert message == """________

guesses    : 
chances    : 7"""
    assert game_over == False

    
def test_correct_input():
    message, game_over = hangman.status_message("elephant", [],'e', 7)
    assert message == """e_e_____

guesses    : e
chances    : 7"""
    assert game_over == False

      
def test_wrong_input():
    message, game_over = hangman.status_message("elephant", ['e'],'x', 6)
    assert message == """e_e_____

guesses    : e x
chances    : 6"""
    assert game_over == False

def test_correct_win_input():
    message, game_over = hangman.status_message("axe", ['e','x','b'],'a', 7)
    assert message == """axe

guesses    : e x b a
chances    : 7
Message    : You Win!!"""
    assert game_over == True


def test_wrong_lose_input():
    message, game_over = hangman.status_message("axe", ['e','x','b'],'y', 0)
    assert message == """_xe

guesses    : e x b y
chances    : 0
Message    : You Lose!! word : axe"""
    assert game_over == True
