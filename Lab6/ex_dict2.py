# Copy Dictionary

x = {1:'Irfan',2:'teh',3:'RUTS'}
print(x)
print(x.keys())

# copy()
y = x
print(y)
y[3] = 'Saiyai'
print(y)
print(x)

y = x.copy()
print(x)
print(y)
y[1] = 'Nattapong'
y[2] = 'Kaewboonma'