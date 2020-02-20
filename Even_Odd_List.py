#Python Program to Put Even and Odd elements in a List into Two Different Lists
print("add even and odd number into List :")
List=[]
even_item=[]
odd_item=[]
for a in input().split():
    List.append(int(a))
for i in List:
    if i%2==0:
       even_item.append(i)
    else:
        odd_item.append(i)

print("*"*20)
print("Even Item List : ",even_item)

print("Odd Item List : ",odd_item)