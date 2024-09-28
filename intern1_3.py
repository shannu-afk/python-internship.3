import random
def choose_word():
    words=["python","coding","portfolio","courses","programming","code","data","visual","studio"]
    return random.choice(words)

def word_status(word,guessed_letters):
    display=""
    for letter in word:
        if letter in guessed_letters:
            display+=letter
        else:
            display+="_"
    return display
def word_guess():
    secret_word=choose_word()
    guessed_letters=[]
    attempts=len(secret_word)
    print("word guessing game")
    print("***************")
    print("HINT:The no.of characters in string is",len(secret_word))
    print("Secret word:",word_status(secret_word,guessed_letters))
    
    while attempts>0:
        guess=input("Guess A letter:").lower()
        if len(guess)!=1 or not guess.isalpha():
            print("You must enter a single letter")
            continue
        if guess in guessed_letters:
            print("You already guessed the letter")
            continue
        guessed_letters.append(guess)
        if guess not in secret_word:
            attempts-=1
            print(f"No letter '{guess}' occurs in the word")
            print(f"You have {attempts} attempts remaining")            
        else:
            occurences=secret_word.count(guess)
            if occurences==1:
                print(f"letter '{guess}' occurs {occurences}st time")
            else:
                print(f"letter '{guess}' occurs {occurences} times")
        current_status=word_status(secret_word,guessed_letters)
        print("secret word:",current_status)
        if "_" not in current_status:
            print("congratulations!You guessed the word")
            break
    if "_" in current_status:
        print(f"You ran out attempts! The word was {secret_word}")
word_guess()
while True:
    user=input("Do you want to Try Again?")
    if user=="yes":
        word_guess()
    else:
        print("Exiting the code")
        break



