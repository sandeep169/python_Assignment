#Python Program to Find the Second Largest Number in a List
List=[]
print("Enter item to add into list :")
for i in input().split():
    List.append(int(i))
print(List)
highest=max(List)
sec_highest=0
for i in List:
    if i>highest:
       highest=i
    if i<highest and i>sec_highest:
        sec_highest=i
print("*"*20)
print("second highest from the list :"+str(sec_highest))