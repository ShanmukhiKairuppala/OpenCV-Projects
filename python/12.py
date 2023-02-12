print("-----if statements-----")

is_Tall = True
if is_Tall:
    print("you are tall")
else:
    print("you are not  tall")

def max_num(num1,num2,num3):
    if num1 >= num2 and num1 >= num3:
        return num1
    elif num2 >= num1 and num2 >=num3:
        return num2
    else:
        return num3
print(max_num(2,4,3))


