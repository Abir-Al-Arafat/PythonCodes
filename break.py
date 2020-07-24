#using break statement to end the current loop and jump to the statement immediately following the loop
while True :
    line = input('Guess the word: ')
    if line == "done" :
        break
    print(line, "is a wrong word")
print('Yay you have guessed the correct word!')