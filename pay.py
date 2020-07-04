#Write a program to prompt the user for hours and rate per hour using input to compute gross pay. Pay the hourly rate for the hours up to 40 and 1.5 times the hourly rate for all hours worked above 40 hours. Use 45 hours and a rate of 10.50 per hour to test the program (the pay should be 498.75). You should use input to read a string and float() to convert the string to a number. Do not worry about error checking the user input - assume the user types numbers properly.

hrs = input("Enter Hours:")  #taking input
rph = input("Rate Per Hour:")#taking input
try:                         #to check if someone's giving a string value 
    h = float(hrs) #converting to float from string
    r = float(rph) #converting to float from string
except:                      #what to do if someone's giving string value
    print("Please give numeric value")
    quit() #stop this code right here if someone gives a string value. without quit() compiler will read line 11 
if (h>40) : 
    h = h - 40
    h = h*15.75
    h = h + (40*r)
    print("payment",h)
else : 
    h = h*r
    print("Payment:",h)