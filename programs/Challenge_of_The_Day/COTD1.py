#def sorting(myString):
 #   words = myString.split()
   # noDuplicates = sorted(set(words))
    #return " ".join(noDuplicates)

#print(sorting("hello world and practice makes perfect and hello world again"))

def sorting(myString):
    words = myString.split()
    noDuplicates = sorted(set(words))
    return " ".join(noDuplicates)

myString = input("Enter: ")
print(sorting(myString))