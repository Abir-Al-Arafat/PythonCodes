#using continue to end the current iteration and jump to the top of the loop and start next iteration.
while True : 
    line = input("guess the word: ")
    if line[0] == "#" :
        continue
    
    if line == "done" :
        break
    print(line,"is a wrong word!")
print("yay",line,"is the right word")
        