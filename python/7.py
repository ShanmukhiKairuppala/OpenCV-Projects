# LISTS
friends=["rita" ,"sita" ,"sheela" ,2, True]   #we can put anything inside of a list 
    #       0      1       2       3   4
    #      -5     -4       -3     -2  -1  
print(friends)
print("\n-------------accessing elements of a list-------------------\n")
print(friends[0])
print(friends[1])
print(friends[2])
print(friends[3])
print(friends[4])
print("\n---------------accessing list from back---------------------\n")
print(friends[-1])#index from back starts with -1
print(friends[-5])
#print(friends[5]) list index out of range
#print(friends[6])
print("\n----------------to access some part of list--------------------\n")
# to access some part of list
print(friends[2:])# to access all the elements coming from index 2
print("\n--------------printing elements in a range---------------\n")
print(friends[1:3]) # prints elements at index 1 and 2 ,excluding 3rd.
print("\n--------------we can change elements in a list----------------------\n")
# we can change elements in a list
friends[2]="tom"
print(friends)
