Subject1 = int(input("Enter your marks(English):"))
Subject2 = int(input("Enter your marks(Maths):"))
Subject3 = int(input("Enter your marks(IT):"))
Total= ((Subject1+Subject2+Subject3)/300)*100
print (round(Total,2))
if(Total > 90):
    print("Well Done, you got A grade" "\n  congratulations!!!")
elif(Total>=80 and Total<=89):
    print("Keep up the good work, You got B grade")
elif(Total>=70 and Total<=79):
    print("You are doing good, You got C grade")
elif(Total>=60 and Total<=69):
    print("Keep the pace high, You got D grade")
else:
    print("Dont worry,Keep Learning. You got F grade")#
