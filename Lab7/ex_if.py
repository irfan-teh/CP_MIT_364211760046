# if statement

print('start')
x = int(input('Enter integer x: '))
y = int(input('Enter integer y: '))
z = int(input('Enter integer z: '))

if x > y and x > z:
    print(f'{x} is more than {y},{z}.')
    if y > z:
        print(f'{y} is more than {z}.')
    elif z > y:
       print(f'{y} is more than {z}.')
    else:
        print(f'{y} and {z} are equal.')
elif y > x and y > z:
    print(f'{y} is more than {x},{z}.')
elif z > x and z > y:
    print(f'{z} is more than {x},{y}.')
elif x==y==z:
    print(f'x={x} y={y} z={z} are equal.')
else:
     print(f'Some value are equal.')

print('end')
