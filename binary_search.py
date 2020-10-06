import math
# This is code for a binary search
# given a sorted list of numbers, the goal is to identify whether or not a number is included 

stuff= []
i="empty"
while i != "stop":
    i= input("Enter a number to add to the list, when done, input stop: ")
    if i!= "stop":
        stuff.append(int(i))
find= int(input("Enter a number to find: "))
print(stuff)
print(find)
low=stuff[0]
high=stuff[len(stuff)-1]
while low!=high:
    mid= int((stuff.index(high)-stuff.index(low))/2)+stuff.index(low)
    print(mid)

    if stuff[mid] == find:
        print("FOUND!")
        exit()
    elif stuff[mid]>find:
        high=stuff[mid-1]
        print("low:", low)
        print("high:", high)
    else:
        low=stuff[mid+1]
        print("low:", low)
        print("high:", high)
if low==find:
    print("FOUND!")
else:
    print("NOT FOUND!")
exit()
