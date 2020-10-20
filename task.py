#Write a program that repeatedly prompts a user for integer numbers until the user enters 'done'. Once 'done' is entered, print out the largest and smallest of the numbers. If the user enters anything other than a valid number catch it with a try,
largest = None
smallest = None
while True:
    num = input("Enter a number: ")
    if num == "done" : 
        break
    try:
        num1 = int(num)
    except:
        print("Invalid!!")
        continue
    
    if largest is None:
        largest = num1
    elif num1>largest:
        largest = num1
    elif smallest is None :
        smallest = num1
    elif num1<smallest :
        smallest = num1

print("Maximum is", largest)
print("Minimum is", smallest)