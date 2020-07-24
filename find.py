#Find a value using boolean variable
print("Finding 3")
for value in [1,2,3,3,4,5,6,7]:
    if value == 3:
        find = True
        print(find,value)
        print(value,"is found!")
        
    else:
        find = False
        print(find,value)
print("Done!")