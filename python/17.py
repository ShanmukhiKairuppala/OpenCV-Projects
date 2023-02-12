# translation to 's' language

def translate( phrase ):
    translation = ""
    for letter in phrase:
        if letter.lower() in "aeiou":# or we can use "letter in "AEIOUaeiou":
            if letter.isupper():   
                translation = translation + "S"
            else:
                translation = translation + "s"
        else:
            translation = translation + letter
    return translation

    

print(translate(input("enter a phrase: ")))
