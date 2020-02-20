#7 . Python Program that Displays which Letters are in the Two Strings but not in Both
first = "heyhellow"
second = "hellowqsss"
new=''
for i in first:
      for j in second:
           if i!=j:
              new=j
              frist=new
new=first+new
print(new)
print(frist)

