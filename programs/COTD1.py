def sorting(myString):
    words = myString.split()
    words.sort()
    noDuplicates = sorted(set(words))
    return " ".join(noDuplicates)

print(sorting("hello world and practice makes perfect and hello world again"))

#def sorting(myString):
 #   myString = input("Enter phrase: ")
  #  words = myString.split()
   # words.sort()
    #return " ".join(words)
