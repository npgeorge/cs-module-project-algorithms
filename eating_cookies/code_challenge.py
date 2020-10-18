# sum all mins
#UPER
#U: sum all mins
#P: iterate through list of lists, pull minimum
# min()
min_list = [[8, 4], [90, -1, 3], [9, 62], [-7, -1, -56, -6], [201], [76, 18]]
empty = []

x = 0
for i in min_list:
    empty.append(min(i))

#print(empty)

x = empty[0]
for i in empty:
    x = x + i

#print(x)
k = 3
this = [1,2,3,4]
print(this[-k:])

