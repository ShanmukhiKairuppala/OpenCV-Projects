print("2d lists and nested loops")
number_grid = [
    [1,2,3],
    [4,5,6],
    [0]
 ]

print(number_grid[0][1])
print("\n")
for x in number_grid:
    print(x)
print("\n")
for row in number_grid:
    for cols in row:
        print(cols,end = " ")