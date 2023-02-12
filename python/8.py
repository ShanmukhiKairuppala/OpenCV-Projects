print("\n-------------LIST FUNCTIONS-------------\n")
numbers=['2','3','4','5','6']
friends=["tom","mike","rita","kevin","oscar"]
print("\n---------------concatenating two lists----------------\n")
friends.extend(numbers)
print(friends)
print("\n---------------append another item into a list--------------\n")
friends.append("karen")   #Adds item at the end of the list
print(friends)
print("\n----------------- To add item in the middle of the list------------\n") 
friends.insert(1,"jim")  # inserts jim at index 1,and all the other elements are pushed one index forward
print(friends)
print("\n-------------to remove any element from the list-----------------\n")
friends.remove("tom")
print(friends)
print("\n-------------to empty the list-----------------\n")
#friends.clear()
#print(friends)
print("\n-------------to pop an element from the list-----------------\n")
friends.pop()   # pops out karen from the list
print(friends)
# if the list is empty it gives Index error
print("\n-------------to find index of an element in the list-----------------\n")
print(friends.index("rita"))
print("\n-------------to check whether an element is present in the list-----------------\n")
#print(friends.index("karen"))
print("\n-------------to check number of times an element is repeated in the list-----------------\n")
friends=['jim', 'mike', 'rita','rita', 'kevin', 'oscar', '2', '3', '4', '5', '6'] # rita is repeated twice
print(friends.count("rita"))
print("\n-------------to sort the list-------------\n")
friends.sort()
numbers.sort()
print(friends)   # sorts list in alphabetical and numerical order
print(numbers)
print("\n-------------to reverse the list-------------\n")
numbers.reverse()
print(numbers)
print("\n-------------to copy a list to another list-------------\n")
example=numbers.copy()
print("example = ",example)