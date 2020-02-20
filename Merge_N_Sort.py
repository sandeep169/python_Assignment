#Python Program to Merge Two Lists and Sort it
List_first = [2,3,23,54,67,89,8,4,6]
List_second = [5,75,39,45,23,46,854,733,234]
print("list first :"+str(List_first))
print("list second :"+str(List_second))

print("*"*50)

Merge_list=List_first +List_second


print("Merged List: ",Merge_list)
Merge_list.sort()
Sorted_list=Merge_list
print ("Sorted List: ",Sorted_list)