#9. Python Program to Print Table of a Given Number
print("Enter the number for  table")
table=int(input())

for i in range(1,11):
    print(str(i)+"*"+str(table)+" = "+str(table*i))
