import random
words=["apple","banana","mango","grapes","orange"]
random_word=random.choice(words)
guess_letter=[]
actual_word=['_' for _ in random_word]
print(" WELLCOME TO HANGMAN GAME!!!\n")
print("RULES:\n")
print("1.guess a single letter in the actual word\n2.It should not contain any digits or special characters.\n3.you have 6 attempts to guess\n")
limit=6
incorrect=0
while incorrect<limit and '_' in actual_word:
    print("word:",' '.join(actual_word))
    guess=input("enter a letter")
    if len(guess)!=1 or not guess.isalpha():
        print("enter a single alphabet")
        continue
    if guess in guess_letter:
        print("you already guessed this letter")
        continue
    guess_letter.append(guess)
    if guess in random_word:
        print("your guess is correct")
        for i in range(len(random_word)):
            if random_word[i]==guess:
                actual_word[i]=guess
    else:
        incorrect+=1
        print("its a wrong guess")
        print("you have ",6-incorrect,"attempts left")
if '_' not in actual_word:
    print("YOU WON!!!!! the word was:",''.join(actual_word))
else:
    print("GAME OVER! the word was:",''.join(actual_word))
    
        
    
    
    

