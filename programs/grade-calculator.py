print("Welcome to Grade Calculator")

maths = int(input("Please enter your maths mark: "))
chemistry = int(input("Please enter your chemistry mark: "))
phys = int(input("Please enter your physics mark: "))

percentage_score = (maths + chemistry + phys) / 3

if percentage_score <40:
    print ("Your percentage score is ", percentage_score,"%")
    print ("You failed")
elif percentage_score >=40 and percentage_score <50:
    print ("Your percentage score is ", percentage_score,"%")
    print ("You scored a grade of: D")
elif percentage_score >=50 and percentage_score <60:
    print ("Your percentage score is ", percentage_score,"%")
    print ("You scored a grade of: C")
elif percentage_score >=60 and percentage_score <70: 
    print ("Your percentage score is ", percentage_score,"%")
    print ("You scored a grade of: B")
elif percentage_score >=70:
    print ("Your percentage score is ", percentage_score,"%")
    print ("You scored a grade of: A")
