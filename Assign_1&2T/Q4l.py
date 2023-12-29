name = input("Enter your name : ")
rollNo = input("Enter your roll number : ")

def grade(num):
    if(num>=80):
        return "O grade"
    elif(num>= 70 and num<80):
        return "A+ grade"
    elif(num>=60 and num<70):
        return "A grade"
    elif(num>=50 and num<60):
        return "B+ grade"
    elif(num>=40 and num<50):
        return "B grade"
    elif(num>=35 and num<40):
        return "C+ grade"
    else:
        return "FAIL"

# def gradesmit(gr):
#     grade = {
#         10: "O",
#         9: "A+",
#         8: "A",
#         7: "B+",
#         6: "B",
#         5: "C+"
#     }
#     if(gr>10 or gr<5):
#         return "fail"
#     else:
#         gr = gr//1
#         return grade[gr]

def creditPoint(num):
    if(num>=80):
        return 10
    elif(num>= 70 and num<80):
        return 9
    elif(num>=60 and num<70):
        return 8
    elif(num>=50 and num<60):
        return 7
    elif(num>=40 and num<50):
        return 6
    elif(num>=35 and num<40):
        return 5
    else:
        return 4
    

def takingNumber(sn):
    num = int(input("Enter the number of " + sn + " : "))
    return num


def takingCredit(sn):
    num = int(input("Enter the credit of " + sn + " : "))
    return num


subj1 = takingNumber("Daa")
subj1_c = takingCredit("Daa")

subj2 = takingNumber("OS")
subj2_c = takingCredit("OS")

subj3 = takingNumber("DBMS")
subj3_c = takingCredit("DBMS")

subj4 = takingNumber("TOC")
subj4_c = takingCredit("TOC")

subj5 = takingNumber("DP")
subj5_c = takingCredit("DP")

total = subj1+subj2+subj3+subj4
percentage = (total/400) * 100

s1_grade = grade(subj1)
s1_score = creditPoint(subj1)
s1_totalPoints = s1_score * subj1_c

s2_grade = grade(subj2)
s2_score = creditPoint(subj2)
s2_totalPoints = s2_score * subj2_c

s3_grade = grade(subj3)
s3_score = creditPoint(subj3)
s3_totalPoints = s3_score * subj3_c

s4_grade = grade(subj4)
s4_score = creditPoint(subj4)
s4_totalPoints = s4_score * subj4_c

s5_grade = grade(subj5)
s5_score = creditPoint(subj5)
s5_totalPoints = s5_score * subj5_c

totalCredit = (subj1_c + subj2_c + subj3_c + subj4_c + subj5_c) 
scoredCredit = s1_totalPoints + s2_totalPoints + s3_totalPoints + s4_totalPoints + s5_totalPoints

sgpa = scoredCredit/totalCredit
print("=====================================================================")
print("Name : " +name+ "\t\t\t\tRoll No : "+rollNo)
print("Programme : B.Tech (Computer Engineering)\tSemester : 1")
print("\n\n")
print("\t\tCourse\t\tCourse Credit\tGrade")
print("Daa\t\t\t\t",subj1_c,"\t\t"+s1_grade)
print("Daa\t\t\t\t",subj2_c,"\t\t"+s2_grade)
print("Daa\t\t\t\t",subj3_c,"\t\t"+s3_grade)
print("Daa\t\t\t\t",subj4_c,"\t\t"+s4_grade)
print("Daa\t\t\t\t",subj5_c,"\t\t"+s5_grade)
print("\n\n\n")
print("SGPA : " ,sgpa)
print("Percentage : " , percentage)
print("=====================================================================")


