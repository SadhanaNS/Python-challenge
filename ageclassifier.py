age = int(input("Enter your age:"))
if(age<=1):
    print("He/she is a infant")
elif(age>=1 and age<=3):
    print("He/she is a toddler")
elif(age>=3 and age<=12):
    print("He/she is a child")
elif(age>=12 and age<=17):
    print("He/she is a Teenager")
elif(age>=18 and age<=60):
    print("He/she is a adult")
else:
    print("He/she is a senior citizen")