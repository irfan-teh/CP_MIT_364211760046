f = open("A4Q1.txt", 'a')
i = int(input("Enter number: "))
count = 0
while count < i:
    if i % 5 == 0:
        count = count + 5
    f.write(str(count)+'\n')
f.close()