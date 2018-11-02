i=1
esum=0
osum=0
while (i<=20):
    if (i%2==0):
        esum=i+esum
        i=i+1
    else:
        osum=i+osum
        i=i+1
print(esum)
print(osum)
