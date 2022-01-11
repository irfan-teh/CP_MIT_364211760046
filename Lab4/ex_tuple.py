# Tuple

mytuple = ('apple','banana','cherry','papaya','orange')
print(tuple)
print(type(mytuple))

# access item in tuple
# index
print(mytuple[0])
print(mytuple[4])
# negative index
print(mytuple[-1])
print(mytuple[-3])
# range index
print(mytuple[2:4])
print(mytuple[:3])
print(mytuple[2:])
# range negative index
print(mytuple[-4:-2])
print(mytuple[-4:])

# loop
# for
for x in  mytuple:
    print(x, end='')
print('\n')

# for whith index
for x in range(len(mytuple)):
    print(mytuple[x])
# while
print('Data in tuple with while loop:')
i = 0
while i < len(mytuple):
    print(mytuple[i])
    i+1

# updata data in tuple
# tranform tuple to list
mylist = list(mytuple)
print(mylist)
print(type(mylist))
# change data in list
mylist[-1] = 'mango'
print(mylist)
# add data in list
mylist.append('apple')
print(mylist)
# remove