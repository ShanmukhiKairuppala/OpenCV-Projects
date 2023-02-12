print("---------Functions---------")
# to print a statement from a function,we need to call the function
def func() :
    print("hello user !!")
func()  #function call
 
def funct(name):
    print("hello "+name)
funct("shanmukhi")

def funct(name,age):
    print("hello "+name+". You are "+age)
funct("shanmukhi","35")

def funct(name,age):
    print("hello "+name+". You are "+str(age)) # converting int to string
funct("shanmukhi",35)