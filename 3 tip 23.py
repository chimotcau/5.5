def f(x,y):
    if x==y:
        return  1
    if x>y or x==17:
        return 0
    if x<y:
        return f(x+1,y) + f(x*2,y)
print (f(1,10) *f(10,21))
#answer:14                