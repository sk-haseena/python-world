#compound interest using recursions
def ci(p,t,r):
    amount=p*(pow((1+r/100),t))
    compin=amount-p
    return compin
p=int(input("enter principle amount:"))
t=int(input("enter no.of years:"))
r=int(input("enter rate:"))
y=1
while y<=t:
    compin=ci(p,y,r)
    print("compound interest of ",y,"years",compin)
    y=y+1
