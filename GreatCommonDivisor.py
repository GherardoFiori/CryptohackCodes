
a = 66528
b = 52920
r=a%b
while r:
    a=b
    b=r
    r=a%b
print('GCD is:', b)