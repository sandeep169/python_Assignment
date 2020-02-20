#7 . Python Program that Displays which Letters are in the Two Strings but not in Both
first = "abcd"
second = "efghda"
new_string=first+second
similar_char=''

print("String First:",first)
print("String Second:",second)

for i in first:
      for j in second:
           if i==j:
              similar_char = j

              new_string = new_string.replace(similar_char,'')

print("*"*20)
print("Concatenated string with no duplicacy :",new_string)




