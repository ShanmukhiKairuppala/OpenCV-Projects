print("-------while loop---------")
i=1
while i<=10:
    print(i)
    i=i+1

print("--------for loop-------")
j=1
for j in range(10):
    print(j)

def power(x,k):
    z=1
    for i in range (k):
        z=z*x
    return z
print(power(2,3))
