#Doing average using a loop
count = 0
sum = 0
print("Before",count,sum)
print("Count","Sum","Values")
for value in [9,3,5,2,1]:
    count = count + 1
    sum = sum + value
    print(count,"    ",sum,"  ",value)
print("Total Values:",count,"After sum: ",sum,"Average:",sum/count)