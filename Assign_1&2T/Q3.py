subj1 = int(input("Enter the number of subject 1 : "))
subj2 = int(input("Enter the number of subject 2 : "))
subj3 = int(input("Enter the number of subject 3 : "))
subj4 = int(input("Enter the number of subject 4 : "))

total = subj1+subj2+subj3+subj4
totalNumber = (total/400) * 100

if(totalNumber>=80):
    print("O grade")
elif(totalNumber>= 70 and totalNumber<80):
    print("A+ grade")
elif(totalNumber>=60 and totalNumber<70):
    print("A grade")
elif(totalNumber>=50 and totalNumber<60):
    print("B+ grade")
elif(totalNumber>=40 and totalNumber<50):
    print("B grade")
else:
    print("You scored less than 40 number!!")

